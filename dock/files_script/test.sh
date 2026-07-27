#!/bin/bash

. /usr/local/bin/asic_status.sh

function debug()
{
	/usr/bin/logger $1
	/bin/echo `date` "- $1" >> ${DEBUG_LOG}
}

function check_warm_boot()
{
	SYSTEM_WARM_START=`$SONIC_DB_CLI STATE_DB 
		hget "WARM_RESTART_ENABLE_TABLE|system" enable`
	SERVICE_WARM_START=`$SONIC_DB_CLI STATE_DB 
		hget "WARM_RESTART_ENABLE_TABLE|${SERVICE}" enable`
	if [[ x"$SYSTEM_WARM_START" == x"true" ]] || [[ x"$SERVICE_WARM_START" == x"true" ]]; then
		WARM_BOOT="true"
	else
		WARM_BOOT="false"
	fi
}

function validate_restore_count()
{
	if [[ x"$WARM_BOOT" == x"true" ]]; then
		RESTORE_COUNT=`$SONIC_DB_CLI STATE_DB hget "WARM_RESTART_TABLE|${SERVICE}" restore_count`
		# We have to make sure db data has not been flushed.
		if [[ -z "$RESTORE_COUNT" ]]; then
			WARM_BOOT="false"
		fi
	fi
}

function check_fast_boot ()
{
	SYSTEM_FAST_REBOOT=`sonic-db-cli STATE_DB hget "FAST_RESTART_ENABLE_TABLE|system" enable`
	if [[ x"${SYSTEM_FAST_REBOOT}" == x"true" ]]; then
		FAST_BOOT="true"
	else
		FAST_BOOT="false"
	fi
}

start() {
	debug "Starting ${SERVICE} service..."

	check_warm_boot
	validate_restore_count

	check_fast_boot

	debug "Warm boot flag: ${SERVICE} ${WARM_BOOT}."
	debug "Fast boot flag: ${SERVICE} ${FAST_BOOT}."

	# Start the test container
	docker run -id --name ${SERVICE} --privileged docker-test:latest
	debug "Started ${SERVICE} service..."
}

wait() 
{
	# Wait for the container to be ready
	debug "Waiting for ${SERVICE} service to be ready..."
	sleep 5  # Adjust this as needed for the container to initialize
	debug "${SERVICE} service is ready."
}

stop() {
	debug "Stopping ${SERVICE} service..."

	check_warm_boot
	check_fast_boot
	debug "Warm boot flag: ${SERVICE} ${WARM_BOOT}."
	debug "Fast boot flag: ${SERVICE} ${FAST_BOOT}."

	if [[ x"$WARM_BOOT" == x"true" ]] || [[ x"$FAST_BOOT" == x"true" ]]; then
		docker kill ${SERVICE} &> /dev/null || debug "Docker ${SERVICE} is not running ($?) ..."
	else
		docker stop ${SERVICE} &> /dev/null || debug "Docker ${SERVICE} is not running ($?) ..."
	fi

	docker rm ${SERVICE} &> /dev/null || debug "Docker ${SERVICE} container already removed ($?) ..."
	debug "Stopped ${SERVICE} service..."
}

SERVICE="test"
DEBUG_LOG="/tmp/${SERVICE}-debug.log"

case "$1" in
	start|wait|stop)
		$1
		;;
	*)
		echo "Usage: $0 {start|wait|stop}"
		exit 1
		;;
esac
