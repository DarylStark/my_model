Models explained
================

A model is a ``Pydantic`` object that is used to describe the scheme of the data in the **My Project**. By using ``Pydantic``, the models get type and value validation. Because the models need to be used in SQLalchemy too, we use the ``SQLmodel`` library. This library uses the ``Pydantic`` library to create models, and the ``SQLAlchemy`` library to create a ORM for SQL databases.

All models are derived from the ``SQLModel`` baseclass. The following UML model describe the inheritance for the classes:

.. mermaid::

   classDiagram

   MyModel <|-- APIScope
   MyModel <|-- User
   Config *-- MyModel : Subclass
   User *-- UserRole : role [enum]
   MyModel <|-- UserScopedModel
   UserScopedModel <|-- TokenModel
   TokenModel <|-- APIClient
   TokenModel <|-- APIToken
   UserScopedModel <|-- Tag
   UserScopedModel <|-- UserSetting

   MyModel : int id
   MyModel : get_random_string()

   Config: bool validate_assignment = True

   APIScope : str module
   APIScope : str subject
   APIScope : str full_scope_name

   User: datetime created
   User: str fullname
   User: str username
   User: str email
   User: UserRole role
   User: str password_hash
   User: datetime password_date
   User: str second_factor
   User: list[APIClient] api_clients
   User: list[APIToken] api_tokens
   User: list[Tag] tags
   User: list[UserSetting] user_settings
   User: void set_password()
   User: str set_random_second_factor()
   User: none diable_second_factor()
   User: bool verify_credentials()

   UserRole: int ROOT = 1
   UserRole: int USER = 2

   UserScopedModel: int user_id

   TokenModel: str token
   TokenModel: str set_random_token()

   APIClient: datetime created
   APIClient: datetime expires
   APIClient: bool enabled
   APIClient: str app_name
   APIClient: str app_publisher
   APIClient: str redirect_url
   APIClient: User user
   APIClient: list[APIToken] api_tokens

   APIToken: datetime created
   APIToken: datetime expires
   APIToken: int api_client_id
   APIToken: bool eanbled
   APIToken: str title
   APIToken: User user
   APIToken: APIClient api_client

   Tag: str title
   Tag: str color
   Tag: User user

   UserSetting: str setting
   UserSetting: str value
   UserSetting: User user

As you can see in the diagram, all models inherit from the ``MyModel`` baseclass. This class has a subclass with the name ``Config`` that configures the ``SQLModel`` and ``Pydantic`` baseclasses. We set the ``validate_assignment`` attribute in this class to make sure assignments are validated. Every model has a integer for the ``id`` via the baseclass ``MyModel``.

On the next page, we describe how **Global Models** are used.