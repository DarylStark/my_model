# New version

This document describes the versioning scheme for this library and describe the steps that are needed when a new version should be released.

## Versioning

This library uses a versioning scheme with the format `MAJOR.MINOR.PATCH[-TAG]`. The `MAJOR` version will be `1`. It will be increased on complete new versions. For instance on a rewrite of the application or when introducing new features that will break the usage of this library. The `MINOR` will be increased every time at least one new feature is added. The `PATCH` will be increased on version with bugfixes only.

The `TAG` can ben any of the following:
-   `dev`; used for the library when it is still in development. This is not a tested release!
-   nothing; for tested releases.

## Create a new version

After we upload a package to the index, we increase the version. This means we create a new `dev` version and start working on that. If all needed code updates are in there, we upload the package with the newly generated version and increase the version again. If we are ready to create a final release, we remove the tag and upload it to the package index. The steps are:

1.  Create a new `dev` version.
    -   If we are going to work on a new `PATCH` version, use the following command:

        ```bash
        bumpver update --tag dev --patch
        ```

    -   If we are going to work on a new `MINOR` version, use the following command:

        ```bash
        bumpver update --tag dev --minor
        ```

2.  Start working on the version. Add the features or bugfixes you want to add.
3.  As soon as everything is in there, we can build the library using the following command:

    ```bash
    python3 -m build
    ```

    The package will be build and placed in the `dist/` folder.
4.  Tag the current commit with the version number (including the tag) and push it to GitHub

    ```bash
    git push origin --tags
    ```

5.  Copy the created package to the package index so other libraries and application can use it.
6.  When the `dev` version is tested completly and we are ready to make it a production version, remove the `-dev` tag with the following command:

    ```bash
    bumpver update --tag final
    ```

7.  After that, build the package:

    ```bash
    python3 -m build
    ```

    The package will be build and placed in the `dist/` folder.
8.  Tag the current commit with the version number and push it to GitHub

    ```bash
    git push origin --tags
    ```
9.  Copy the created package to the package index so other libraries and application can use it.
