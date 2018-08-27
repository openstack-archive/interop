#!/bin/bash

tempestdir=$(mktemp -d)
echo $tempestdir
git clone git://git.openstack.org/openstack/tempest $tempestdir


PYTHONPATH=$tempestdir python ./tools/checktests.py --guideline next.json
exit_1=$?

PYTHONPATH=$tempestdir python ./tools/checktests.py --guideline 2018.02.json
exit_2=$?

PYTHONPATH=$tempestdir python ./tools/checktests.py --guideline 2017.09.json
exit_3=$?

rm -rf $tempestdir

! (( $exit_1 || $exit_2 || $exit_3 ))
