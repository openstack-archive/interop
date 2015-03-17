OpenStack DefCore Lexicon
=========================================


Licensing the OpenStack commercial-use marks requires passing tests of
DefCore required capabilities, and including designated sections of code.
There are multiple marks available for vendors depending on which
capability groupings are passed.

TERMS:
----------------------------------------

Core
  Word to be avoided in this process due to confusion with other
  uses.

DefCore
  The OpenStack board committee that manages commercial definition
  of OpenStack for trademark purposes.

DefCore Process
  The process used by DefCore to score capabilities and
  select criteria.

Designated Sections
  Portions of the OpenStack codebase that must be used to provide
  required capabilities in a product wishing to use the OpenStack
  trademark.  Designated sections fulfill one or more of the following
  criteria: they provide the project-external REST API, or are shared
  and provide common functionality for all options, or implement logic
  that is critical for cross-platform operation.  Designated sections
  must exist in the OpenStack gerrit namespace and have corresponding
  tests.  Code that meets the following criteria will not be considered
  designated: provides vendor-specific functionality, are explicitly
  intended by the project maintainers to be replaceable, extend the
  project REST API in a new or different way, or code that is being
  deprecated.
 
Guidelines
  Output of the DefCore process detailing which sections and
  capabilities are required.  Guidelines will be approved on a regular
  cadence and identified by the date of approval.

Capability
  The functionality ensured by a set of tests collected into
  a group as defined by the DefCore committee Required - capabilities that
  are required to meet the guideline.

Advisory
  Capabilities that have been suggested for the next guideline.

Deprecated
  Capabilities that will be removed in the next guideline.

Component
  A collection of functionality generally used together (e.g.:
  object, compute).

Platform
  The collection of components required to use the least restricted mark.
 
OpenStack Mark
  Right granted by the OpenStack Foundation to use the name and logo of
  OpenStack in a vendor’s product.

Test
  Program that exercises functionality of a component to validate
  expected behavior and provides pass or fail judgement.

Flagged Test
  A test that does not provide consistent results in the
  field and it not required for vendor self-test * Self-test - process by
  which a vendor runs tests against their product or service without 3rd
  party observation.

Certify or Accredit
  DefCore does not do any of these things for OpenStack clouds.  These
  actions would fall under the governance of the Foundation trademark
  policy.
