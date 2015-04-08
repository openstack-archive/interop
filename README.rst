=================================================
Understanding the DefCore Guidelines
=================================================

This repository contains DefCore committee managed files that provide guidance for the OpenStack community.

NOTE: Changes to file requires approval of the DefCore committee chair(s).


DefCore Process Flow
====================

see /process/2015A.rst or later

Terminology
====================

see lexicon.rst

JSON Schema
==================== 

The JSON files have a specific schema to support 

.. code-block:: json

  { "id": "2015.03",        # Spec name (date based)
    "source": "http://git.openstack.org/cgit/openstack/defcore/",   # git repo for files
    "schema": "1.2",        # Schema version
    "status": "approved",   # can be draft, review or approved
    "replaces": "2014.07",  # previous spec
    "releases": ["icehouse"], # array of releases, lower case
    "platform": {           # platform components
      "required": ["compute", "object"],  # array
      "advisory": [],       # incoming array
      "depricated": [],     # outgoing array
      "removed": []         # removed array
      },
    "components": {         # components detail
      "compute": {          # component name
        "required": [       # required array
          "compute-auth"],
        "advisory": [       # incoming array
          "compute-servers-metadata"],
        "deprecated": [],   # outgoing array
        "removed": [        # removed array
          "volume"]
        },
      },
    "criteria" : {          # explains achievements
        "atomic" : { "Description" : "blah blah blah",
        "name" : "Atomic", 
        "weight": 8
        },
    "capabilities": {       # capabilities listed in components
      "example-cap" :       # capability
        { "achievements" :  # array of criteria met
          [ "deployed",
            "future",
            "complete"],
        "admin" : false,    # is admin API
        "status" : "required",  # de-normalized from components
        "description" : "Helpful Description",
        "flagged" : [  ],   # flagged tests array
        "name" : "Friendly Short Name",
        "tests" :           # list of tests (please use UUIDs)
          [ "tempest.api.project.file.class.test_name" ]
      },

