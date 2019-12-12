from typing import Any, ClassVar, Generator, List, Optional, Union, Text, Iterable, Sequence, Type

class ObjectIdentifier(object):
    def __init__(self, dotted_string: str) -> None: ...
    def dotted_string(self) -> str: ...


class CRLEntryExtensionOID(object):
    CERTIFICATE_ISSUER: ClassVar[ObjectIdentifier]
    CRL_REASON: ClassVar[ObjectIdentifier]
    INVALIDITY_DATE: ClassVar[ObjectIdentifier]

class ExtensionOID(object):
    AUTHORITY_INFORMATION_ACCESS: ClassVar[ObjectIdentifier]
    AUTHORITY_KEY_IDENTIFIER: ClassVar[ObjectIdentifier]
    BASIC_CONSTRAINTS: ClassVar[ObjectIdentifier]
    CERTIFICATE_POLICIES: ClassVar[ObjectIdentifier]
    CRL_DISTRIBUTION_POINTS: ClassVar[ObjectIdentifier]
    CRL_NUMBER: ClassVar[ObjectIdentifier]
    DELTA_CRL_INDICATOR: ClassVar[ObjectIdentifier]
    EXTENDED_KEY_USAGE: ClassVar[ObjectIdentifier]
    FRESHEST_CRL: ClassVar[ObjectIdentifier]
    INHIBIT_ANY_POLICY: ClassVar[ObjectIdentifier]
    ISSUER_ALTERNATIVE_NAME: ClassVar[ObjectIdentifier]
    ISSUING_DISTRIBUTION_POINT: ClassVar[ObjectIdentifier]
    KEY_USAGE: ClassVar[ObjectIdentifier]
    NAME_CONSTRAINTS: ClassVar[ObjectIdentifier]
    OCSP_NO_CHECK: ClassVar[ObjectIdentifier]
    POLICY_CONSTRAINTS: ClassVar[ObjectIdentifier]
    POLICY_MAPPINGS: ClassVar[ObjectIdentifier]
    PRECERT_POISON: ClassVar[ObjectIdentifier]
    PRECERT_SIGNED_CERTIFICATE_TIMESTAMPS: ClassVar[ObjectIdentifier]
    SUBJECT_ALTERNATIVE_NAME: ClassVar[ObjectIdentifier]
    SUBJECT_DIRECTORY_ATTRIBUTES: ClassVar[ObjectIdentifier]
    SUBJECT_INFORMATION_ACCESS: ClassVar[ObjectIdentifier]
    SUBJECT_KEY_IDENTIFIER: ClassVar[ObjectIdentifier]
    TLS_FEATURE: ClassVar[ObjectIdentifier]

class NameOID(object):
    BUSINESS_CATEGORY: ClassVar[ObjectIdentifier]
    COMMON_NAME: ClassVar[ObjectIdentifier]
    COUNTRY_NAME: ClassVar[ObjectIdentifier]
    DN_QUALIFIER: ClassVar[ObjectIdentifier]
    DOMAIN_COMPONENT: ClassVar[ObjectIdentifier]
    EMAIL_ADDRESS: ClassVar[ObjectIdentifier]
    GENERATION_QUALIFIER: ClassVar[ObjectIdentifier]
    GIVEN_NAME: ClassVar[ObjectIdentifier]
    JURISDICTION_COUNTRY_NAME: ClassVar[ObjectIdentifier]
    JURISDICTION_LOCALITY_NAME: ClassVar[ObjectIdentifier]
    JURISDICTION_STATE_OR_PROVINCE_NAME: ClassVar[ObjectIdentifier]
    LOCALITY_NAME: ClassVar[ObjectIdentifier]
    ORGANIZATIONAL_UNIT_NAME: ClassVar[ObjectIdentifier]
    ORGANIZATION_NAME: ClassVar[ObjectIdentifier]
    POSTAL_ADDRESS: ClassVar[ObjectIdentifier]
    POSTAL_CODE: ClassVar[ObjectIdentifier]
    PSEUDONYM: ClassVar[ObjectIdentifier]
    SERIAL_NUMBER: ClassVar[ObjectIdentifier]
    STATE_OR_PROVINCE_NAME: ClassVar[ObjectIdentifier]
    STREET_ADDRESS: ClassVar[ObjectIdentifier]
    SURNAME: ClassVar[ObjectIdentifier]
    TITLE: ClassVar[ObjectIdentifier]
    USER_ID: ClassVar[ObjectIdentifier]
    X500_UNIQUE_IDENTIFIER: ClassVar[ObjectIdentifier]


class OCSPExtensionOID(object):
    NONCE: ClassVar[ObjectIdentifier]


class SignatureAlgorithmOID(object):
    DSA_WITH_SHA1: ClassVar[ObjectIdentifier]
    DSA_WITH_SHA224: ClassVar[ObjectIdentifier]
    DSA_WITH_SHA256: ClassVar[ObjectIdentifier]
    ECDSA_WITH_SHA1: ClassVar[ObjectIdentifier]
    ECDSA_WITH_SHA224: ClassVar[ObjectIdentifier]
    ECDSA_WITH_SHA256: ClassVar[ObjectIdentifier]
    ECDSA_WITH_SHA384: ClassVar[ObjectIdentifier]
    ECDSA_WITH_SHA512: ClassVar[ObjectIdentifier]
    ED25519: ClassVar[ObjectIdentifier]
    ED448: ClassVar[ObjectIdentifier]
    RSASSA_PSS: ClassVar[ObjectIdentifier]
    RSA_WITH_MD5: ClassVar[ObjectIdentifier]
    RSA_WITH_SHA1: ClassVar[ObjectIdentifier]
    RSA_WITH_SHA224: ClassVar[ObjectIdentifier]
    RSA_WITH_SHA256: ClassVar[ObjectIdentifier]
    RSA_WITH_SHA384: ClassVar[ObjectIdentifier]
    RSA_WITH_SHA512: ClassVar[ObjectIdentifier]

