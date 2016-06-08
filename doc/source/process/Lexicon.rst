OpenStack Interop Working Group Lexicon
========================================


Licensing the OpenStack commercial-use marks requires passing tests of
required capabilities, and including designated sections of code.
There are multiple marks available for vendors depending on which
capability groupings are passed.

TERMS:
----------------------------------------

Advisory
  Capabilities that have been suggested for the next Guideline.

Capability
  The functionality ensured by a set of tests collected into
  a group as defined by the Interop Working Group.

Certify or Accredit
  The Interop Working Group does not do any of these things
  for OpenStack clouds. These actions would fall under the
  governance of the Foundation trademark policy.

Community
  The universe of people and companies that are involved in the OpenStack
  project as active contributors, users, operators, vendors and enthusiasts.
  This is a very broad group with diverse interests, needs and participation
  levels. (see also Participant)

Component
  A collection of functionality generally used together (e.g.:
  object, compute).

Contributor
  Word to be avoided in this process due to confusion with other uses.

Core
  Word to be avoided in this process due to confusion with other
  uses.

DefCore
  The original name for the OpenStack board committee that managed
  commercial definition of OpenStack for trademark purposes. As the
  group evolved, it's name was eventually changed to the Interop
  Working Group.

Deprecated
  Capabilities that will be removed in the next Guideline.

Designated Sections
  Portions of the OpenStack codebase that must be used to provide
  required capabilities in a product wishing to use the OpenStack
  trademark. Designated sections fulfill one or more of the following
  criteria: they provide the project-external REST API, or are shared
  and provide common functionality for all options, or implement logic
  that is critical for cross-platform operation. Designated sections
  must exist in the OpenStack gerrit namespace and have corresponding
  tests. Code that meets the following criteria will not be considered
  designated: provides vendor-specific functionality, are explicitly
  intended by the project maintainers to be replaceable, extend the
  project REST API in a new or different way, or code that is being
  deprecated.

Flagged Test
  A test that does not provide consistent results in the
  field and it not required for vendor self-test.

Guidelines
  Output of the Interop Working Group process detailing which
  Designated Sections and Capabilities are required. Guidelines will be
  approved on a regular cadence and identified by the date of approval.

Interop Working Group Process
  The process used by the Interop Working Group to score Capabilities
  and select Criteria.

OpenStack Mark
  Right granted by the OpenStack Foundation to use the name and logo of
  OpenStack in a vendor’s product.

Participant
  The subset of the Community that actively engages in creating
  components of OpenStack including, but not limited to, the code,
  documentation, training, product management and other materials.
  For Interop Working Group purposes, Participant is not limited to
  the community members identified as "ATC" as per
  http://git.openstack.org/cgit/openstack/governance/tree/reference/charter.rst#n132
  (see also Technical Leadership)

Platform
  The collection of components required to use the least restricted mark.

Removed
  Capabilities that are no longer required and are not included in the
  current Guideline.

Required - Capabilities that are required to be exposed to end users to
  satisfy the requirements of an Interoperability Guideline.

Self-test
  Process by which a vendor runs tests against their product or service
  without 3rd party observation.

Technical Leadership
  The subset of the Participants (see above) that are recognized by the
  community to guide the technical direction of the OpenStack project.
  These leaders include the Technical Committee (TC) and Project
  Technical Leads (PTL).
  See: http://git.openstack.org/cgit/openstack/governance/tree/reference/charter.rst

Test
  Program that exercises functionality of a component to validate
  expected behavior and provides pass or fail judgement.
