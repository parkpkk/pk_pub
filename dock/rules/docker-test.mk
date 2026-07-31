#============================================================
# Docker image for TEST (test feature engine)
# ============================================================

# Base name for the image layers
DOCKER_TEST_STEM = docker-test
DOCKER_TEST = $(DOCKER_TEST_STEM).gz
DOCKER_TEST_DBG = $(DOCKER_TEST_STEM)-$(DBG_IMAGE_MARK).gz

# Path to the docker build directory (where Dockerfile is located)
$(DOCKER_TEST)_PATH = $(DOCKERS_PATH)/docker-test

# === MAIN DEPENDENCIES ===
# Direct binary package dependencies are omitted. Core container construction depends exclusively on base environment synchronization.
(DOCKER_TEST)_DEPENDS += 

# Dependencies for the symbol-stripped DEBUG container layer
(DOCKER_TEST)_DBG_DEPENDS = $($(DOCKER_CONFIG_ENGINE_BOOKWORM)_DBG_DEPENDS)
(DOCKER_TEST)_DBG_DEPENDS += $(LIBSWSSCOMMON) $(PYTHON3_SWSSCOMMON)

# Extra utility packages to dynamically inject inside the DEBUG image
(DOCKER_TEST)_DBG_IMAGE_PACKAGES = $($(DOCKER_CONFIG_ENGINE_BOOKWORM)_DBG_IMAGE_PACKAGES)

# Inject the standard SONiC Python common wheels required for database orchestration
(DOCKER_TEST)_PYTHON_WHEELS =
(DOCKER_TEST)_PYTHON_WHEELS += $(SONIC_PY_COMMON_PY3)

# Establish the standard target base Linux engine distribution layer
$(DOCKER_TEST)_LOAD_DOCKERS += $(DOCKER_CONFIG_ENGINE_BOOKWORM)

# System Package Metadata 
$(DOCKER_TEST)_VERSION = 1.0.0
$(DOCKER_TEST)_PACKAGE_NAME = test

#
## === REGISTER WITH THE SYSTEM BUILD PIPELINE ===
#
SONIC_DOCKER_IMAGES += $(DOCKER_TEST)
SONIC_INSTALL_DOCKER_IMAGES += $(DOCKER_TEST)

SONIC_DOCKER_DBG_IMAGES += $(DOCKER_TEST_DBG)
SONIC_INSTALL_DOCKER_DBG_IMAGES += $(DOCKER_TEST_DBG)

# Register target targets with Debian Bookworm compile suite
SONIC_BOOKWORM_DOCKERS += $(DOCKER_TEST)
SONIC_BOOKWORM_DBG_DOCKERS += $(DOCKER_TEST_DBG)

#
## === RUNTIME ISOLATION CONFIGURATION ===
#
$(DOCKER_TEST)_CONTAINER_NAME = test

# Grant deep network manipulation privileges to allow the daemon 
# to bind sockets and track hardware interface events natively.
$(DOCKER_TEST)_RUN_OPT += -t --privileged --cap-add=NET_ADMIN

# Standard immutable read-only system configurations and timezone volume mapping bounds
$(DOCKER_TEST)_RUN_OPT += -v /etc/sonic:/etc/sonic:ro
$(DOCKER_TEST)_RUN_OPT += -v /etc/localtime:/etc/localtime:ro 
#
# Hook the standard process life-cycle exit listener monitoring script
$(DOCKER_TEST)_FILES += $(SUPERVISOR_PROC_EXIT_LISTENER_SCRIPT)

