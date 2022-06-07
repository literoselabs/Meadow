from fastapi import APIRouter
import requests

router = APIRouter(prefix='/api/net', tags=['api', 'net'])

@router.get('/public_ipv4')
def get_public_ipv4():
    resp = requests.get('http://ipv4.icanhazip.com/')
    if resp.status_code != 200:
        return {'ipv4': None, 'error': resp.status_code}
    else:
        return {'ipv4': resp.content.strip()}

@router.get('/public_ipv6')
def get_public_ipv4():
    resp = requests.get('http://ipv6.icanhazip.com/')
    if resp.status_code != 200:
        return {'ipv6': None, 'error': resp.status_code}
    else:
        return {'ipv6': resp.content.strip()}