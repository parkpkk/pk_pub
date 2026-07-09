import re
import json
import os
import subprocess
import xmltodict
from datetime import date

class YangIntegratedStandardizer:
    def __init__(self, target_yang):
        self.target_yang = target_yang
        self.type_db = {}        
        self.identity_map = {}   
        self.path_type_map = {}  
        self.list_keys_map = {} 
        self.path_args = []

    def build_db(self, root_dir='models'):
        """GIỮ NGUYÊN: Quét và xây dựng cơ sở dữ liệu kiểu dữ liệu."""
        print(f"🚀 Scanning all YANG files in '{root_dir}'...")
        search_paths = set()
        yang_files = []
        for root, dirs, files in os.walk(root_dir):
            if any(f.endswith('.yang') for f in files):
                search_paths.add(root)
            for file in files:
                if file.endswith('.yang'):
                    yang_files.append(os.path.join(root, file))

        self.path_args = []
        for p in search_paths:
            self.path_args.extend(["-p", p])

        for f_path in yang_files:
            try:
                res = subprocess.run(["pyang", "-f", "yin"] + self.path_args + [f_path], capture_output=True, text=True)
                if res.returncode != 0: continue
                data = xmltodict.parse(res.stdout)
                root_node = data.get('module') or data.get('submodule')
                if root_node: self._deep_scan(root_node)
            except: continue
        print(f"✅ DB built: {len(self.type_db)} types, {len(self.identity_map)} identities.")

    def _deep_scan(self, obj):
        """GIỮ NGUYÊN: Duyệt sâu Identity và Typedef."""
        if not isinstance(obj, dict): return
        if 'identity' in obj:
            ids = obj['identity'] if isinstance(obj['identity'], list) else [obj['identity']]
            for i in ids:
                base_v = i.get('base')
                base = base_v.get('@name', 'ROOT').split(':')[-1] if isinstance(base_v, dict) else (str(base_v).split(':')[-1] if base_v else 'ROOT')
                if base not in self.identity_map: self.identity_map[base] = []
                self.identity_map[base].append(i.get('@name'))
        
        if 'typedef' in obj:
            tds = obj['typedef'] if isinstance(obj['typedef'], list) else [obj['typedef']]
            for td in tds:
                name = td.get('@name', '').lower()
                info = self._extract_deep_info(td)
                if info: self.type_db[name] = info

        for tag in ['leaf', 'leaf-list', 'grouping', 'container', 'list', 'uses']:
            if tag in obj:
                items = obj[tag] if isinstance(obj[tag], list) else [obj[tag]]
                for item in items:
                    name = item.get('@name', '').lower()
                    info = self._extract_deep_info(item)
                    if info: self.path_type_map[name] = info
                    self._deep_scan(item)

    def _extract_deep_info(self, node):
        """GIỮ NGUYÊN: Trích xuất ENUM, NUM, IDENTITYREF."""
        if not isinstance(node, dict): return None
        t_node = node.get('type')
        if not t_node: return None
        t_type = t_node.get('type')
        if isinstance(t_type, list):
            results = [self._extract_deep_info({'type': sub_t}) for sub_t in t_type]
            return " | ".join(dict.fromkeys(filter(None, results)))
        
        t_name = t_node.get('@name', '')
        if t_name == 'leafref':
            return f"LEAFREF_PATH:{t_node.get('path', {}).get('@value', '')}"
        if t_name in ['enumeration', 'enum'] or 'enum' in t_node:
            enums = t_node.get('enum', [])
            if isinstance(enums, dict): enums = [enums]
            return f"ENUM:({', '.join([e['@name'] for e in enums if '@name' in e])})"
        if 'range' in t_node:
            r_val = t_node['range'].get('@value', '').replace('..', '-')
            return f"NUM({r_val})"
        if t_name == 'identityref':
            base_v = t_node.get('base', {})
            base = base_v.get('@name', '').split(':')[-1] if isinstance(base_v, dict) else str(base_v).split(':')[-1]
            return f"IDENTITY_BASE:{base}"
        return t_name.upper() if t_name else None

    def resolve_type(self, leaf_name, raw_meta, current_path, visited=None):
        """GIỮ NGUYÊN: Logic Resolve Type."""
        if visited is None: visited = set()
        leaf_l = leaf_name.lower()
        if leaf_l in visited: return "string"
        visited.add(leaf_l)

        clean_meta = raw_meta.split()[0].replace('?', '').replace('*', '').split(':')[-1].lower() if raw_meta else ""
        res = self.type_db.get(clean_meta) or self.path_type_map.get(leaf_l)
        
        if res and isinstance(res, str) and "LEAFREF_PATH" in res:
            target_leaf = res.split('/')[-1].split(':')[-1].lower()
            if target_leaf != leaf_l:
                return self.resolve_type(target_leaf, "", current_path, visited)
            return "string"

        if res and "|" in str(res):
            parts = str(res).split(" | ")
            resolved_parts = []
            for p in parts:
                if "IDENTITY_BASE" in p:
                    base = p.split(':')[-1].strip()
                    resolved_parts.append(f"<{ '|'.join(self.identity_map.get(base, ['string'])) }>")
                else: resolved_parts.append(p)
            return " | ".join(resolved_parts)

        if res and "IDENTITY_BASE" in str(res):
            base = res.split(':')[-1].strip()
            all_vals = self.identity_map.get(base, ["string"])
            if 'icmpv4' in current_path.lower():
                all_vals = [v for v in all_vals if any(x in v.lower() for x in ['v4', 'echo', 'dst'])]
            elif 'icmpv6' in current_path.lower():
                all_vals = [v for v in all_vals if any(x in v.lower() for x in ['v6', 'neighbor'])]
            return f"<{ '|'.join(list(dict.fromkeys(all_vals))) }>"
        
        final_val = str(res) if res else (clean_meta.upper() if clean_meta else "string")
        if "->" in final_val or "IDENTITYREF" in final_val.upper():
            return "string"
        return final_val

    def _smart_join(self, parts):
        """GIỮ NGUYÊN: Gộp tên thông minh."""
        if not parts: return "main_group"
        clean = []
        for p in parts:
            p = p.lower()
            if p in ['config', 'state']: continue
            if clean and (p in clean[-1] or clean[-1] in p):
                clean[-1] = p
                continue
            clean.append(p)
        return "_".join(clean)

    def parse_universal_to_4_levels(self, module_root_name):
        """CHỈ SỬA: Đổi tên container gốc trùng module_root_name."""
        try:
            tree_out = subprocess.check_output(["pyang", "-f", "tree"] + self.path_args + [self.target_yang]).decode('utf-8')
        except: return {}
        lines = tree_out.strip().split('\n')
        node_pattern = re.compile(r'^(.*?)[+\-| ]+--(?:rw|ro|--)?\s+([\w\-\:\*]+)(?:\?|)?\s*(.*)$')
        result = {}
        # Ép root name đầu tiên trùng tên module
        result[module_root_name] = {}
        stack = [] 

        for line in lines:
            match = node_pattern.match(line)
            if not match: continue
            depth = match.start(0) + match.group(0).find('--')
            raw_name, raw_meta = match.group(2), match.group(3).strip()
            base_name = raw_name.replace('*', '').split(':')[-1].lower()
            is_list_node = '*' in raw_name
            
            # Root ảo để mapping vào module_root_name
            if not stack:
                stack = [(depth, base_name, is_list_node)]
                continue

            while stack and stack[-1][0] >= depth: stack.pop()
            stack.append((depth, base_name, is_list_node))

            if is_list_node:
                found_keys = re.findall(r'\[(.*?)\]', raw_meta)
                if found_keys:
                    self.list_keys_map[base_name] = found_keys[0].split()

            if raw_meta and not any(c in raw_meta for c in ['+', '|']):
                list_idx = -1
                for i in range(len(stack)-1, -1, -1):
                    if stack[i][2]: 
                        list_idx = i
                        break
                full_path_str = "/".join([s[1] for s in stack])
                resolved_type = self.resolve_type(base_name, raw_meta, full_path_str)
                
                if list_idx != -1:
                    l3_name = stack[list_idx][1]
                    if base_name == l3_name: continue
                    l2_parts = [s[1] for s in stack[1:list_idx]]
                    l2_name = self._smart_join(l2_parts)
                    
                    # SỬA: Viết hoa Level 2 và Level 3
                    l2_key = l2_name.upper()
                    l3_key = l3_name.upper()

                    if l2_key not in result[module_root_name]: result[module_root_name][l2_key] = {}
                    if l3_key not in result[module_root_name][l2_key]:
                        result[module_root_name][l2_key][l3_key] = {}
                        if l3_name not in self.list_keys_map:
                            self.list_keys_map[l3_key] = ["id"]
                        else:
                            # Map key gốc sang tên mới viết hoa
                            self.list_keys_map[l3_key] = self.list_keys_map[l3_name]

                    result[module_root_name][l2_key][l3_key][base_name.upper()] = f"{{{resolved_type}}}"
                else:
                    l2_key = "COMMON_SETTINGS"
                    if l2_key not in result[module_root_name]: result[module_root_name][l2_key] = {}
                    result[module_root_name][l2_key][base_name.upper()] = f"{{{resolved_type}}}"
        return result

    def export_yang(self, data):
        """GIỮ NGUYÊN: Xuất file YANG, Indent chuẩn, bù Key."""
        output = ""
        for root, l2_dict in data.items():
            output += f"    container {root} {{\n"
            for l2, l3_dict in l2_dict.items():
                output += f"        container {l2} {{\n"
                for l3_name, l3_val in l3_dict.items():
                    if isinstance(l3_val, dict):
                        keys_list = self.list_keys_map.get(l3_name, ["id"])
                        keys_str = " ".join(keys_list).lower()
                        output += f"            list {l3_name} {{\n"
                        output += f"                key \"{keys_str}\";\n"
                        existing_leaves = [k.lower() for k in l3_val.keys()]
                        for kn in keys_list:
                            if kn.lower() not in existing_leaves:
                                output += f"                leaf {kn.lower()} {{ type string; }}\n"
                        for f4_name, f4_type in l3_val.items():
                            output += self._format_leaf(f4_name.lower(), f4_type, 4)
                        output += "            }\n"
                    else: output += self._format_leaf(l3_name.lower(), l3_val, 3)
                output += "        }\n"
            output += "    }\n"
        return output

    def _format_single_type(self, t_str, indent_level):
        """GIỮ NGUYÊN: Format Type sang Enum/Range."""
        space = "    " * indent_level
        inner = ""
        if t_str.startswith("<") and t_str.endswith(">"):
            inner += f"{space}type enumeration {{\n"
            vals = t_str.strip("<>").split("|")
            for v in vals: inner += f"{space}    enum \"{v.strip()}\";\n"
            inner += f"{space}}}\n"
            return inner
        if "ENUM" in t_str:
            inner += f"{space}type enumeration {{\n"
            match = re.search(r'\((.*)\)', t_str)
            if match:
                for en in match.group(1).split(', '): inner += f"{space}    enum \"{en}\";\n"
            inner += f"{space}}}\n"
        elif "NUM" in t_str:
            match = re.search(r'\((.*)\)', t_str)
            inner += f"{space}type uint32 {{\n"
            if match: inner += f"{space}    range \"{match.group(1).replace('-', '..')}\";\n"
            inner += f"{space}}}\n"
        else:
            clean_t = t_str.strip("<>").split('|')[0].strip().lower()
            inner += f"{space}type {clean_t if clean_t else 'string'};\n"
        return inner

    def _format_type_block(self, t_str, indent_level):
        """GIỮ NGUYÊN: Hỗ trợ Union."""
        parts = [p.strip() for p in t_str.split(" | ") if p.strip()]
        if len(parts) > 1:
            res = "    " * indent_level + "type union {\n"
            for p in parts: res += self._format_single_type(p, indent_level + 1)
            res += "    " * indent_level + "}\n"
            return res
        return self._format_single_type(parts[0], indent_level)

    def _format_leaf(self, name, type_str, indent_level):
        """GIỮ NGUYÊN: Format Leaf."""
        space = "    " * indent_level
        t = type_str.strip("{}")
        res = f"{space}leaf {name} {{\n"
        res += self._format_type_block(t, indent_level + 1)
        res += f"{space}}}\n"
        return res

if __name__ == "__main__":
    import_mk = "import.mk"
    yang_targets = []
    current_date = date.today().strftime("%Y-%m-%d")

    if os.path.exists(import_mk):
        with open(import_mk, "r") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"): continue
                yang_targets.append(line)
    
    if not yang_targets:
        print(f"⚠️ No active YANG files found in {import_mk}")
    else:
        print("🛠️ Pre-building Type Database...")
        base_manager = YangIntegratedStandardizer(yang_targets[0])
        base_manager.build_db(root_dir='models')

        for target_path in yang_targets:
            print(f"\n🔄 Processing: {target_path}")
            filename = os.path.basename(target_path).replace(".yang", "")
            module_name = f"sonic-{filename}"

            manager = YangIntegratedStandardizer(target_path)
            manager.type_db = base_manager.type_db
            manager.identity_map = base_manager.identity_map
            manager.path_type_map = base_manager.path_type_map
            manager.path_args = base_manager.path_args

            # TRUYỀN module_name để làm root container
            tree_data = manager.parse_universal_to_4_levels(module_name)
            
            if tree_data:
                header = (
                    f"module {module_name} {{\n"
                    f"    namespace \"http://github.com/sonic-net/openconfig/{module_name}\";\n"
                    f"    prefix {module_name};\n"
                    f"    yang-version 1.1;\n\n"
                    f"    import ietf-inet-types {{\n"
                    f"        prefix inet;\n"
                    f"    }}\n\n"
                    f"    organization\n"
                    f"        \"SONiC\";\n\n"
                    f"    contact\n"
                    f"        \"SONiC\";\n\n"
                    f"    description\n"
                    f"        \"SONIC OPENCONFIG YANG AUTO CONVERTION FOR {filename.upper()}\";\n\n"
                    f"    revision {current_date} {{\n"
                    f"        description\n"
                    f"            \"Initial revision generated by YangIntegratedStandardizer.\";\n"
                    f"    }}\n"
                )
                
                body = manager.export_yang(tree_data)
                yang_content = f"{header}\n{body}\n}}"
                
                output_filename = f"{module_name}.yang"
                with open(output_filename, "w") as f: f.write(yang_content)
                print(f"✅ Successfully created: {output_filename}")