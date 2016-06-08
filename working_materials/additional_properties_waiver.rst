============================
Additional Properties Waiver
============================

In mid-2015, the OpenStack QA team implemented strict response
checking as an implementation detail and enforcement of Nova
microversions. Microversions, in development since the Kilo release of
OpenStack, were designed to allow for backwards compatible additions
to the API, giving both client and server the option to request and
receive responses within a known range of capabilities. In support
of the interoperability goals of microversions and compatbility between
OpenStack clouds, the QA team introduced strict API response checking of
Nova calls as part of tempest-lib.

Prior to this change, clouds running the Nova 2.0 API could take
advantage of a mechanism to add extensions to the Nova endpoint, and
some also sent additional data back in their Nova responses. These clouds
passed interoperability testing when the OpenStack Powered program was
launched. After strict response checking was added to Tempest, these
clouds failed interop testing.

To address this issue, and the challenges vendors have in updating their
products to match upstream API changes, this proposal offers a means for
vendors to pass the interoperability tests while proving
compatibility for required capabilities.

There is a natural tension between the forward motion of upstream
development and the product requirements of downstream deployments. This
proposal attempts to reconcile that tension by extending the time that
vendors will be required to remove additional properties and replace
those features with alternatives. Possible resolutions for downstream
products include, but are not limited to:

#. Removal of all additional properties.
#. Contributing micro-version changes upstream to capture additional
   properties.
#. Using custom HTTP headers to request additional properties, to be
   used by custom clients or tools.
#. Deploying additional endpoints that return unmodified responses.
#. Remaining on the Nova v/2.0 API, which has been removed from the
   Newton release of OpenStack

This waiver program will cover the 2015.07, 2016.01, and 2016.08
interoperability guidelines, and give downstream vendors a year
to work internally and within the ecosystem to update their products
before re-verifying their products.

It's important to note that the Nova team has for two years been
broadcasting their intentions[1][2][3], offering microversions as an
interoperable way to add new data, and has removed the 2.0 API and
extensions code from the Newton release. Although no known clients
implement strict response checking (except for the Tempest client),
it is clearly the direction that upsteam OpenStack developers have
signaled.

=================
Details of Waiver
=================

#. Products appyling for the OpenStack Powered Trademark in 2016 may
   request the waiver by submitting subunit data from their Tempest run
   that can be analyzed by the `find_additional_properties.py` script
   from the Interop WG's git repository. This script will identify
   tests that failed because of additional properties. The vendor will
   then need to modify tempest-lib[4] to remove additional checks on
   the impacted APIs. Development is beginning within the
   refstack-client project[5] to automate generation of a patch for
   tempest-lib.

#. Products that use additional properties in Nova API responses will be
   clearly identified in the OpenStack Marketplace, with the product
   listing showing which APIs have included additional response data.
   Products using additional data will be restricted to the Nova 2.0 API.

#. Beginning with the 2017.01 release of the Interoperability Guideline,
   this waiver program will no longer be in force, unless 'additional
   properties' is listed as an acceptable implementation using the Nova
   2.0 API in the forthcoming capabilities list. All other new
   products must pass upstream testing.

#. Aside from additional properties, no products may change the json API
   response in any other way.

[1] http://lists.openstack.org/pipermail/openstack-dev/2015-February/057613.html
[2] https://specs.openstack.org/openstack/nova-specs/specs/kilo/implemented/api-microversions.html
[3] http://lists.openstack.org/pipermail/openstack-dev/2015-March/059576.html
[4] https://github.com/openstack/tempest/tree/master/tempest/lib/api_schema/response/compute
[5] http://git.openstack.org/cgit/openstack/refstack-client/
