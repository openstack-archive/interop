=====================
Platform Capabilities
=====================

Platform and Program Capabilities
=================================

::

   The following was approved by the OpenStack Board.

Extend the DefCore principles to allow for multiple levels: programs and
platforms. Programs represent subsections of the overall platform. In some
cases, it is acceptable for a program identified without being included in
the platform. New programs are added at Foundation recommendation via board
approval. Programs are added to the platform via board approval.

The initial programs will be Compute & Object. The DefCore platform will
require the Compute program, Object program and additional capabilities.

Havana Approved: The Compute Program will consist of the following
capabilities:

* compute-servers

* compute-volume

* compute-quotas

* compute-flavors

* compute-auth

* compute-keypairs

* compute-servers-metadata

* compute-floating-ips

* compute-images

* compute-instance-actions

* compute-security-groups

Havana Approved: The Object Program will consist of the following
capabilities:

* objectstore-object,

* objectstore-container

Havana Approved:: The Platform will consist of all the capabilities in the
Compute and Object programs and the following capabilities:

* images-v1

* volume

* volume-snapshots

Platform and Components Illustration
====================================

.. image:: ../images/DefCore_Platform_and_Programs_v14.jpg
