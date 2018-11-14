#!/bin/bash

# This script will run consistency checks for Tempest tests against
# the three latest interoperability guidelines. It can run in two
# modes.
#
# * If no arguments are specified, the script will check out Tempest
#   into a temporary directory, run the consistency checks, then delete
#   temporary checkout.
#
# * If an argument is given, this script will assume that it is a
#   user checked-out repository and run the consistency checks against
#   that, and leave the directory unchanged on exit. This mode is useful
#   for gate jobs and Tempest development.

set -x

if [ ! $@ ]; then
  TEMPESTDIR=$(mktemp -d)
  git clone git://git.openstack.org/openstack/tempest $TEMPESTDIR
  CLEANTEMPEST=cleantempest
else
  TEMPESTDIR=${1}
fi

PYTHONPATH=$TEMPESTDIR python ./tools/checktests.py --guideline next.json
exit_1=$?

PYTHONPATH=$TEMPESTDIR python ./tools/checktests.py --guideline 2018.02.json
exit_2=$?

PYTHONPATH=$TEMPESTDIR python ./tools/checktests.py --guideline 2018.11.json
exit_3=$?

if [[ ! -z "${CLEANTEMPEST}" ]]; then
  rm -rf $TEMPESTDIR
fi


! (( $exit_1 || $exit_2 || $exit_3 ))
