# -*- coding: utf-8 -*-
#
# Copyright (c) 2022, Globex Corporation
# All rights reserved.
#
from typing import List

from connect.client import ConnectClient
from connect.eaas.core.decorators import (
    router,
    web_app,
)
from connect.eaas.core.extension import WebApplicationBase
from connect.eaas.core.inject.synchronous import get_extension_client
from fastapi import Depends

from connect_ext.schemas import Marketplace


@web_app(router)
class HubTestHugeWebApplication(WebApplicationBase):

    @router.get(
        '/marketplaces',
        summary='List all available marketplaces',
        response_model=List[Marketplace],
    )
    def list_marketplaces(
        self,
        client: ConnectClient = Depends(get_extension_client),
    ):
        return [
            Marketplace(**marketplace)
            for marketplace in client.marketplaces.all().values_list(
                'id', 'name', 'description', 'icon',
            )
        ]
