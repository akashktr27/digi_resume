from django.utils.deprecation import MiddlewareMixin
from Home.models import *
from django.urls import resolve
from celery import shared_task
import requests

class ClientMetadataMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if hasattr(request, '_metadata_saved'):
            return

        # Collect client metadata
        ip_address = self.get_client_ip(request)
        user_agent = request.META.get('HTTP_USER_AGENT', '')
        referrer = request.META.get('HTTP_REFERER', '')

        resolver_match = resolve(request.path_info)
        view_name = resolver_match.view_name

        locals = ['localhostss', '1s27.0.0.1ss']
        if ip_address in locals:
            pass
        else:
            if view_name == 'save_contact':
                # Save POST request metadata to the PostRequestMetadata model
                post_data = request.POST.dict()  # Convert POST data to a dictionary
                PostRequestMetadata.objects.create(
                    ip_address=ip_address,
                    user_agent=user_agent,
                    referrer=referrer,
                    post_data=str(post_data)  # Save POST data as a string
                )
            elif view_name == 'download':  # Replace with your specific view name
                region_name = "NULL"
                try:
                    ip_address = "5.151.123.125"
                    response = requests.get(
                        f"http://api.ipstack.com/{ip_address}?access_key=a501e6be75e9deb3e600c1eba5fc59d2")
                    data = response.json()
                    region_name = data["region_name"]
                except Exception as e:
                    region_name = "NULL"
                    print(f"Error fetching IP details: {e}")

                ResumeViewMetadata.objects.create(
                    ip_address=ip_address,
                    user_agent=user_agent,
                    referrer=referrer,
                    view_name=view_name,
                    resume_region_name=region_name
                )
            elif view_name == 'index':
                # Save general request metadata to the ClientMetadata model


                ClientMetadata.objects.create(
                    ip_address=ip_address,
                    user_agent=user_agent,
                    referrer=referrer,
                )
                # fetch_and_save_ip_details.delay(metadata.id, ip_address)

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]  # Take the first IP in the list
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip



@shared_task
def fetch_and_save_ip_details(metadata_id, ip_address):
    try:
        ip_address = "5.151.123.125"
        response = requests.get(f"http://api.ipstack.com/{ip_address}?access_key=a501e6be75e9deb3e600c1eba5fc59d2")
        data = response.json()
        print(data.region_name)
        ClientMetadata.objects.filter(id=metadata_id).update(region_name=data.region_name)
    except Exception as e:
        print(f"Error fetching IP details: {e}")