from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.workflow import Workflow
from ...types import Response


def _get_kwargs(
    workflow_id: UUID,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/workflow/{workflow_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, Workflow]]:
    if response.status_code == 200:
        response_200 = Workflow.from_dict(response.json())

        return response_200
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, Workflow]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    workflow_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, Workflow]]:
    """Get a workflow

    Args:
        workflow_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Workflow]]
    """

    kwargs = _get_kwargs(
        workflow_id=workflow_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workflow_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, Workflow]]:
    """Get a workflow

    Args:
        workflow_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Workflow]
    """

    return sync_detailed(
        workflow_id=workflow_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    workflow_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, Workflow]]:
    """Get a workflow

    Args:
        workflow_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Workflow]]
    """

    kwargs = _get_kwargs(
        workflow_id=workflow_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workflow_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, Workflow]]:
    """Get a workflow

    Args:
        workflow_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Workflow]
    """

    return (
        await asyncio_detailed(
            workflow_id=workflow_id,
            client=client,
        )
    ).parsed
