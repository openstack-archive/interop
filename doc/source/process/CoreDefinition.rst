===============
Core Definition
===============

Objective
=========

The following list represents the "guiding principles" used by the
Foundation Board to determine how commercial implementations of OpenStack
can be granted use of the trademark. They will continue to get refined over
the next 6 months as the to-be-renamed-Core-Definition Committee refines
the must-pass test selection process and governance. They committee may
suggest changes to the by-laws to clarify the definition of core.

::

   Principles Adopted at Oct 4th 2013 Board Meeting

Implementation
==============

* The `Governance/DefCoreCommittee
  <https://wiki.openstack.org/wiki/Governance/DefCoreCommittee/>`_ is
  working to manage this.
* Meetings and agendas will be posted to that page, hosted on Google
  Hangouts and (generally) open to the community.
* Meeting participants will be expected to commit to the full set of
  meetings, be familiar with the Spider process materials, and up-to-date
  on the committee resolutions to date.
* Havana must-pass tests approved by Ice House Release Ice House must-pass
  tests approved by Ice House Release +90

Principles
==========

.. image:: ../images/500px-Core_flow.png

1. Implementations that are Core can use OpenStack trademark (OpenStack™)

   1. This is the legal definition of "core" and the why it matters to the
      community.

   2. We want to make sure that the OpenStack™ mark means something.

   3. The OpenStack™ mark is not the same as the OpenStack brand; however,
      the Board uses it’s control of the mark as a proxy to help manage the
      brand.

2. Core is a subset of the whole project

   1. The OpenStack project is supposed to be a broad and diverse community
      with new projects entering incubation and new implementations being
      constantly added. This innovation is vital to OpenStack but separate
      from the definition of Core.

   2. There may be other marks that are managed separately by the
      foundation, and available for the platform ecosystem as per the
      Board’s discretion

   3. "OpenStack API Compatible" mark not part of this discussion and
      should be not be assumed.

3. Core definition can be applied equally to all usage models

   1. There should not be multiple definitions of OpenStack depending on
      the operator (public, private, community, etc)

   2. While expected that each deployment is identical, the differences
      must be quantifiable

4. Claiming OpenStack requiring use of designated upstream code

   1. Implementation’s claiming the OpenStack™ mark must use the OpenStack
      upstream code (or be using code submitted to upstream)

   2. You are not OpenStack, if you pass all the tests but do not use the
      API framework

   3. This also surfaces bit-rot in alternate implementations to the larger
      community

   4. This behavior improves interoperability because there is more shared
      code between implementation

5. Projects must have an open reference implementation

   1. OpenStack will require an open source reference base plug-in
      implementation for projects (if not part of OpenStack, license model
      for reference plug-in must be compatible).

   2. Definition of a plug-in: alternate backend implementations with a
      common API framework that uses common _code_ to implement the API

   3. This expects that projects (where technically feasible) are expected
      to implement a plug-in or extension architecture.

   4. This is already in place for several projects and addresses around
      ecosystem support, enabling innovation

   5. Reference plug-ins are, by definition, the complete capability set.
      It is not acceptable to have "core" features that are not functional
      in the reference plug-in

   6. This will enable alternate implementations to offer innovative or
      differentiated features without forcing changes to the reference
      plug-in implementation

   7. This will enable the reference to expand without forcing other
      alternate implementations to match all features and recertify

6. Vendors may substitute alternate implementations

   1. If a vendor plug-in passes all relevant tests then it can be
      considered a full substitute for the reference plug-in

   2. If a vendor plug-in does NOT pass all relevant test then the vendor
      is required to include the open source reference in the
      implementation.

   3. Alternate implementations may pass any tests that make sense

   4. Alternate implementations should add tests to validate new
      functionality.

   5. They must have all the must-pass tests (see #10) to claim the
      OpenStack mark.

   6. OpenStack Implementations are verified by open community tests

   7. Vendor OpenStack implementations must achieve 100% of must-have
      coverage?

   8. Implemented tests can be flagged as may-have requires list [Joshua
      McKenty]

   9. Certifiers will be required to disclose their testing gaps.

   10. This will put a lot of pressure on the Tempest project

   11. Maintenance of the testing suite to become a core Foundation
       responsibility. This may require additional resources

   12. Implementations and products are allowed to have variation based on
       publication of compatibility

   13. Consumers must have a way to determine how the system is different
       from reference (posted, discovered, etc)

   14. Testing must respond in an appropriate way on BOTH pass and fail
       (the wrong return rejects the entire suite)

7. Tests can be remotely or self-administered

   1. Plug-in certification is driven by Tempest self-certification model

   2. Self-certifiers are required to publish their results

   3. Self-certified are required to publish enough information that a 3rd
      party could build the reference implementation to pass the tests.

   4. Self-certified must include the operating systems that have been
      certified

   5. It is preferred for self-certified implementation to reference an
      OpenStack reference architecture "flavor" instead of defining their
      own reference. (a way to publish and agree on flavors is needed)

   6. The Foundation needs to define a mechanism of dispute resolution. (A
      trust but verify model)

   7. As an ecosystem partner, you have a need to make a "works against
      OpenStack" statement that is supportable

   8. API consumer can claim working against the OpenStack API if it works
      against any implementation passing all the "must have" tests(YES)

   9. API consumers can state they are working against the OpenStack API
      with some "may have" items as requirements

   10. API consumers are expected to write tests that validate their
       required behaviors (submitted as "may have" tests)

8. A subset of tests are chosen by the Foundation as "must-pass"

   1. How? Read the `Governance/CoreCriteria <./CoreCriteria.rst/>`_ Selection
      Process

   2. An OpenStack body will recommend which tests are elevated from
      may-have to must-have

   3. The selection of "must-pass" tests should be based on quantifiable
      information when possible.

   4. Must-pass tests should be selected from the existing body of
      "may-pass" tests. This encourages people to write tests for cases
      they want supported.

   5. We will have a process by which tests are elevated from may to must
      lists

   6. Potentially: the User Committee will nominate tests that elevated to
      the board

   7. OpenStack Core means passing all "must-pass" tests

9. The OpenStack board owns the responsibility to define 'core' – to
   approve 'musts'

   1. The "CoreDef" committee will submit the must-pass tests to the board
      as a block and passed as a single motion

   2. We are NOT defining which items are on the list in this effort, just
      making the position that it is how we will define core

   3. May-have tests include items in the integrated release, but which are
      not core.

   4. Must haves – must comply with the Core criteria defined from the
      IncUp committee results

   5. Projects in Incubation or pre-Incubation are not to be included in
      the 'may' list

10. OpenStack Core means passing all "must-pass" tests

    1. The OpenStack board owns the responsibility to define 'core' – to
       approve 'musts'

    2. We are NOT defining which items are on the list in this effort, just
       making the position that it is how we will define core

    3. May-have tests include items in the integrated release, but which
       are not core.

    4. Must haves – must comply with the Core criteria defined from the
       IncUp committee results

    5. Projects in Incubation or pre-Incubation are not to be included in
       the 'may' list
