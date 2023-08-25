.. my-model documentation master file, created by
   sphinx-quickstart on Mon Jul 31 21:34:50 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to my-model's documentation!
====================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:
   :hidden:

   installation
   models
   global
   user_scoped

.. toctree::
   :caption: Developing
   :hidden:
   :maxdepth: 2

   developing/setting_up
   developing/development

.. toctree::
   :caption: API documentation
   :hidden:
   :maxdepth: 2

   api_documentation/my_model
   api_documentation/global_models
   api_documentation/user_scoped_models

The ``my-model`` Python library provides the datamodel for the **My Project**. This model is to be used by all services in the **My Project** that need to do anything with data. The library used the ``SQLModel`` Python library to define the models. This way, they can be used with ``SQLModel`` to create a SQL database abstraction layer.

Types of models
---------------

The library contains two types of models:

* Models that are not bound to a specific user, also called **Global Models**
* Models that are bound to a specific user, also called **User Scoped Models**

In the page `Models explained <models.html>`_, it is explained how models in general are implemented. In `Global model <global.html>`_, it is explained how global models work. In `User scoped models <user_scoped.html>`_, it is explained how user scoped models work.

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
