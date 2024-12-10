import os, sys, re, json, time, uuid, random, requests
from faker import Faker 
from datetime import datetime
from rich.console import Console
from bs4 import BeautifulSoup as bs

# Warna  Ansi 
m = "\033[0;31m" 
p = "\033[0;37m" 
h = "\033[0;32m" 
k = "\033[1;33m"

requests.packages.urllib3.disable_warnings()  

headersPost = {
      'authority': 'm.facebook.com',
      'content-length': '9383',
      'sec-ch-ua': 'Not/A)Brand";v="8", "Chromium";v="125", "Google Chrome";v="125"',
      'sec-ch-ua-mobile': '?1',
      'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Mobile Safari/537.36',
      'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
      'sec-ch-prefers-color-scheme': 'light',
      'sec-ch-ua-platform': '"Android"',
      'accept': '*/*',
      'origin': 'https://m.facebook.com',
      'sec-fetch-site': 'same-origin',
      'sec-fetch-mode': 'cors',
      'sec-fetch-dest': 'empty',
      'referer': 'https://m.facebook.com/reg/',
      'accept-encoding': 'gzip, deflate',
      'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
}
    
headersGet = {
      'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
      'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
      'cache-control': 'max-age=0',
      'dpr': '2',
      'referer': 'https://m.facebook.com/',
      'sec-ch-prefers-color-scheme': 'light',
      'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="125", "Google Chrome";v="125"',
      'sec-ch-ua-mobile': '?1',
      'sec-ch-ua-platform': '"Android"',
      'sec-fetch-dest': 'document',
      'sec-fetch-mode': 'navigate',
      'sec-fetch-site': 'same-origin',
      'sec-fetch-user': '?1',
      'upgrade-insecure-requests': '1',
      'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Mobile Safari/537.36',
      'viewport-width': '980'
}

class RequLink:
    def __init__(self) -> None:
        pass
        
    def Bahasa(self, cookies):
        with requests.Session() as r:
            try:
                response = r.get("https://mbasic.facebook.com/language/", cookies={'cookie':cookies}).text
                payload = bs(response, "html.parser")
                for x in payload.find_all('form',{'method':'post'}):
                    if "Bahasa Indonesia" in str(x):
                        bahasa = {"fb_dtsg" : re.search('name="fb_dtsg" value="(.*?)"',str(response)).group(1),"jazoest" : re.search('name="jazoest" value="(.*?)"', str(response)).group(1), "submit"  : "Bahasa Indonesia"}
                        byps = r.post("https://mbasic.facebook.com/{x['action']}", data=bahasa, cookies={'cookie':cookies})
                return (byps)
            except: pass

    def FLCookies(self, cookies):
        with requests.Session() as r:
            try:
                response = bs(r.get('https://mbasic.facebook.com/profile.php?id=100067687546217',cookies={"cookie": cookies}).text, 'html.parser')
                if "/a/subscribe.php" in str(response):
                     cari = re.search('/a/subscribe.php(.*?)"', str(response)).group(1).replace("amp;", "")
                     byps = r.get("https://mbasic.facebook.com/a/subscribe.php{}".format(cari), cookies={"cookie": cookies})
                return (byps)
            except: pass
        
    def ReactPost(self, cookies):
        with requests.Session() as r:
            try:
                response = bs(r.get('https://mbasic.facebook.com/100067687546217?v=timeline',cookies={"cookie": cookies}).text, 'html.parser')
                for x in response.find_all('a',href=True):
                    if 'Tanggapi' in x.text:
                        tpr = random.choice(['Super','Wow','Peduli','Marah'])
                        for z in bs(r.get('https://mbasic.facebook.com%s'%(x['href']),cookies={"cookie": cookies}).text,'html.parser').find_all('a'):
                            if tpr == z.text:
                                byps = r.get('https://mbasic.facebook.com'+z['href'],cookies={"cookie": cookies})
                return (byps)
            except: pass
            
class Requ:
    def __init__(self):
        self.ses = requests.Session()      
        
    def createMail(self):
        try:
            headers = {
                'User-Agent':'Temp%20Mail/30 CFNetwork/1220.1 Darwin/20.3.0',
                'Content-Type':'application/json'
            }
            data = {
                "name":self.firstnama+self.lastnama+str(random.randint(1000, 9999)),
                "domain":random.choice(requests.get("https://api.internal.temp-mail.io/api/v4/domains", headers={"accept": "application/json, text/plain, */*"}).json()['domains'])['name']
            }
            response = self.ses.post('https://api.internal.temp-mail.io/api/v3/email/new',headers=headers,json=data,verify=False)
            self.mail = response.json()['email']
            return(self.mail)
        except AttributeError as e: return None
        
class RequKd:
    def __init__(self):
        self.ses = requests.Session()
        
    def Kodekonfirmasi(self, mail):
        self.mail = mail
        try:
            headers = {
                'User-Agent':'Temp%20Mail/30 CFNetwork/1220.1 Darwin/20.3.0',
                'Content-Type':'application/json'
            }
            while True:
                response = self.ses.get(f'https://api.internal.temp-mail.io/api/v3/email/{self.mail}/messages', headers=headers,verify=False)
                if 'Facebook' in response.text:
                    for messages in response.json():
                        subject = messages['subject']
                        kode = subject.split(' adalah kode konfirmasi Facebook Anda')[0]
                        return(kode)
                        break
                else: return(None)
        except AttributeError as e: return None
                
class Require:
  def __init__(self):
    self.fake = Faker("id_ID")
    self.uid = str(uuid.uuid4())
    self.uid1 = str(uuid.uuid4())
    self.uid2 = str(uuid.uuid4())
    self.firstnama, self.lastnama = self.depan()
    self.tgl = self.birthday()
    self.gender = str(random.randint(1,2))
    self.timer = str(round(time.time()))
    self.pw = "pilu00"
        
  def depan(self):
    dep = self.fake.first_name_male()
    bel = self.fake.last_name_female()
    return dep, bel
    
  def birthday(self):
    day = str(random.randint(1,28))
    month = str(random.randint(1,12))
    year = str(random.randint(1998,2005))
    return  f"{day}-{month}-{year}"
    
  def ResponseSM(self):
    return(self.firstnama,self.lastnama, self.pw, self.tgl)
        
  def ResponseAkun(self):
    return (f"""        
        {m}firstname{p}:{h} {self.firstnama}
        {m}lastname{p}: {h}{self.lastnama} 
        {m}fullname{p}: {h}{self.firstnama} {self.lastnama}
        {m}password{p}: {h}{self.pw}
        {m}birthday{p}: {h}{self.tgl}""")
        
  def ResponseAkun2(self):
    return (f"""        
        {m}firstname{p}:{k} {self.firstnama}
        {m}lastname{p}: {k}{self.lastnama} 
        {m}fullname{p}: {k}{self.firstnama} {self.lastnama}
        {m}password{p}: {k}{self.pw}
        {m}birthday{p}: {k}{self.tgl}""")

  def data_nama(self):
    return {
      "params": json.dumps({
        "server_params": json.dumps({
          "event_request_id": "{}".format(self.uid),
          "reg_info": json.dumps({
            "first_name": None,
            "last_name": None,
            "full_name": None,
            "contactpoint": None,
            "ar_contactpoint": None,
            "contactpoint_type": None,
            "is_using_unified_cp": None,
            "unified_cp_screen_variant": None,
            "is_cp_auto_confirmed": False,
            "is_cp_auto_confirmable": False,
            "confirmation_code": None,
            "birthday": None,
            "did_use_age": None,
            "gender": None,
            "use_custom_gender": False,
            "custom_gender": None,
            "encrypted_password": None,
            "username": None,
            "username_prefill": None,
            "fb_conf_source": None,
            "device_id": None,
            "ig4a_qe_device_id": None,
            "family_device_id": None,
            "nta_eligibility_reason": None,
            "ig_nta_test_group": None,
            "user_id": None,
            "safetynet_token": None,
            "safetynet_response": None,
            "machine_id": None,
            "profile_photo": None,
            "profile_photo_id": None,
            "profile_photo_upload_id": None,
            "avatar": None,
            "email_oauth_token_no_contact_perm": None,
            "email_oauth_token": None,
            "email_oauth_tokens": None,
            "should_skip_two_step_conf": None,
            "openid_tokens_for_testing": None,
            "encrypted_msisdn": None,
            "encrypted_msisdn_for_safetynet": None,
            "cached_headers_safetynet_info": None,
            "should_skip_headers_safetynet": None,
            "headers_last_infra_flow_id": None,
            "headers_last_infra_flow_id_safetynet": None,
            "headers_flow_id": None,
            "was_headers_prefill_available": None,
            "sso_enabled": None,
            "existing_accounts": None,
            "used_ig_birthday": None,
            "sync_info": None,
            "create_new_to_app_account": None,
            "skip_session_info": None,
            "ck_error": None,
            "ck_id": None,
            "ck_nonce": None,
            "should_save_password": None,
            "horizon_synced_username": None,
            "fb_access_token": None,
            "horizon_synced_profile_pic": None,
            "is_identity_synced": False,
            "is_msplit_reg": None,
            "user_id_of_msplit_creator": None,
            "dma_data_combination_consent_given": None,
            "xapp_accounts": None,
            "fb_device_id": None,
            "fb_machine_id": None,
            "ig_device_id": None,
            "ig_machine_id": None,
            "should_skip_nta_upsell": None,
            "big_blue_token": None,
            "skip_sync_step_nta": None,
            "caa_reg_flow_source": None,
            "ig_authorization_token": None,
            "full_sheet_flow": False,
            "crypted_user_id": None,
            "is_caa_perf_enabled": False,
            "is_preform": True,
            "ignore_suma_check": False,
            "ignore_existing_login": False,
            "ignore_existing_login_from_suma": False,
            "ignore_existing_login_after_errors": False,
            "suggested_first_name": None,
            "suggested_last_name": None,
            "suggested_full_name": None,
            "replace_id_sync_variant": None,
            "is_redirect_from_nta_replace_id_sync_variant": False,
            "frl_authorization_token": None,
            "post_form_errors": None,
            "skip_step_without_errors": False,
            "existing_account_exact_match_checked": False,
            "existing_account_fuzzy_match_checked": False,
            "email_oauth_exists": False,
            "confirmation_code_send_error": None,
            "is_too_young": False,
            "source_account_type": None,
            "whatsapp_installed_on_client": False,
            "confirmation_medium": None,
            "source_credentials_type": None,
            "source_cuid": None,
            "source_account_reg_info": None,
            "soap_creation_source": None,
            "source_account_type_to_reg_info": None,
            "registration_flow_id": "",
            "should_skip_youth_tos": False,
            "is_youth_regulation_flow_complete": False,
            "is_on_cold_start": False,
            "email_prefilled": False,
            "cp_confirmed_by_auto_conf": False,
            "auto_conf_info": None,
            "in_sowa_experiment": False,
            "youth_regulation_config": None,
            "conf_allow_back_nav_after_change_cp": None,
            "conf_bouncing_cliff_screen_type": None,
            "conf_show_bouncing_cliff": None,
            "eligible_to_flash_call_in_ig4a": False,
            "flash_call_permissions_status": None,
            "attestation_result": None,
            "request_data_and_challenge_nonce_string": None,
            "confirmed_cp_and_code": None,
            "notification_callback_id": None,
            "reg_suma_state": 0,
            "is_msplit_neutral_choice": False,
            "msg_previous_cp": None,
            "ntp_import_source_info": None,
            "youth_consent_decision_time": None,
            "username_screen_experience": "control",
            "reduced_tos_test_group": "control",
            "should_show_spi_before_conf": True,
            "google_oauth_account": None,
            "is_reg_request_from_ig_suma": False,
            "is_igios_spc_reg": False,
            "device_emails": None,
            "is_toa_reg": False,
            "is_threads_public": False,
            "spc_import_flow": False,
            "caa_play_integrity_attestation_result": None,
            "flash_call_provider": None,
            "name_prefill_variant": "control",
            "spc_birthday_input": False,
            "failed_birthday_year_count": None,
            "user_presented_medium_source": None
          }),
          "flow_info": json.dumps({
            "flow_name": "new_to_family_fb_default",
            "flow_type": "ntf"
          }),
          "current_step": 1,
          "INTERNAL__latency_qpl_marker_id": 36707139,
          "INTERNAL__latency_qpl_instance_id": "1192247000052",
          "device_id": None,
          "family_device_id": None,
          "waterfall_id": "{}".format(self.uid1),
          "offline_experiment_group": None,
          "layered_homepage_experiment_group": None,
          "is_platform_login": 0,
          "is_from_logged_in_switcher": 0,
          "is_from_logged_out": 0,
          "access_flow_version": "F2_FLOW",
          "INTERNAL_INFRA_THEME": "harm_f"
        }),
        "client_input_params": json.dumps({
          "firstname": "{}".format(self.firstnama),
          "lastname": "{}".format(self.lastnama),
          "lois_settings": json.dumps({
            "lois_token": "",
            "lara_override": ""
          })
        })
      })
    }
    
  def response_nama(self):
    return {
      "params": json.dumps({
          "server_params": json.dumps({
              "waterfall_id": "{}".format(self.uid1),
              "is_platform_login": 0,
              "is_from_logged_out": 0,
              "access_flow_version": "F2_FLOW",
              "reg_info": json.dumps({
                  "first_name": "{}".format(self.firstnama),
                  "last_name": "{}".format(self.lastnama),
                  "full_name": None,
                  "contactpoint": None,
                  "ar_contactpoint": None,
                  "contactpoint_type": None,
                  "is_using_unified_cp": None,
                  "unified_cp_screen_variant": None,
                  "is_cp_auto_confirmed": False,
                  "is_cp_auto_confirmable": False,
                  "confirmation_code": None,
                  "birthday": None,
                  "did_use_age": None,
                  "gender": None,
                  "use_custom_gender": False,
                  "custom_gender": None,
                  "encrypted_password": None,
                  "username": None,
                  "username_prefill": None,
                  "fb_conf_source": None,
                  "device_id": None,
                  "ig4a_qe_device_id": None,
                  "family_device_id": None,
                  "nta_eligibility_reason": None,
                  "ig_nta_test_group": None,
                  "user_id": None,
                  "safetynet_token": None,
                  "safetynet_response": None,
                  "machine_id": None,
                  "profile_photo": None,
                  "profile_photo_id": None,
                  "profile_photo_upload_id": None,
                  "avatar": None,
                  "email_oauth_token_no_contact_perm": None,
                  "email_oauth_token": None,
                  "email_oauth_tokens": None,
                  "should_skip_two_step_conf": None,
                  "openid_tokens_for_testing": None,
                  "encrypted_msisdn": None,
                  "encrypted_msisdn_for_safetynet": None,
                  "cached_headers_safetynet_info": None,
                  "should_skip_headers_safetynet": None,
                  "headers_last_infra_flow_id": None,
                  "headers_last_infra_flow_id_safetynet": None,
                  "headers_flow_id": None,
                  "was_headers_prefill_available": None,
                  "sso_enabled": None,
                  "existing_accounts": None,
                  "used_ig_birthday": None,
                  "sync_info": None,
                  "create_new_to_app_account": None,
                  "skip_session_info": None,
                  "ck_error": None,
                  "ck_id": None,
                  "ck_nonce": None,
                  "should_save_password": None,
                  "horizon_synced_username": None,
                  "fb_access_token": None,
                  "horizon_synced_profile_pic": None,
                  "is_identity_synced": False,
                  "is_msplit_reg": None,
                  "user_id_of_msplit_creator": None,
                  "dma_data_combination_consent_given": None,
                  "xapp_accounts": None,
                  "fb_device_id": None,
                  "fb_machine_id": None,
                  "ig_device_id": None,
                  "ig_machine_id": None,
                  "should_skip_nta_upsell": None,
                  "big_blue_token": None,
                  "skip_sync_step_nta": None,
                  "caa_reg_flow_source": None,
                  "ig_authorization_token": None,
                  "full_sheet_flow": False,
                  "crypted_user_id": None,
                  "is_caa_perf_enabled": False,
                  "is_preform": True,
                  "ignore_suma_check": False,
                  "ignore_existing_login": False,
                  "ignore_existing_login_from_suma": False,
                  "ignore_existing_login_after_errors": False,
                  "suggested_first_name": None,
                  "suggested_last_name": None,
                  "suggested_full_name": None,
                  "replace_id_sync_variant": None,
                  "is_redirect_from_nta_replace_id_sync_variant": False,
                  "frl_authorization_token": None,
                  "post_form_errors": None,
                  "skip_step_without_errors": False,
                  "existing_account_exact_match_checked": False,
                  "existing_account_fuzzy_match_checked": False,
                  "email_oauth_exists": False,
                  "confirmation_code_send_error": None,
                  "is_too_young": False,
                  "source_account_type": None,
                  "whatsapp_installed_on_client": False,
                  "confirmation_medium": None,
                  "source_credentials_type": None,
                  "source_cuid": None,
                  "source_account_reg_info": None,
                  "soap_creation_source": None,
                  "source_account_type_to_reg_info": None,
                  "registration_flow_id": "",
                  "should_skip_youth_tos": False,
                  "is_youth_regulation_flow_complete": False,
                  "is_on_cold_start": False,
                  "email_prefilled": False,
                  "cp_confirmed_by_auto_conf": False,
                  "auto_conf_info": None,
                  "in_sowa_experiment": False,
                  "youth_regulation_config": None,
                  "conf_allow_back_nav_after_change_cp": None,
                  "conf_bouncing_cliff_screen_type": None,
                  "conf_show_bouncing_cliff": None,
                  "eligible_to_flash_call_in_ig4a": False,
                  "flash_call_permissions_status": None,
                  "attestation_result": None,
                  "request_data_and_challenge_nonce_string": None,
                  "confirmed_cp_and_code": None,
                  "notification_callback_id": None,
                  "reg_suma_state": 0,
                  "is_msplit_neutral_choice": False,
                  "msg_previous_cp": None,
                  "ntp_import_source_info": None,
                  "youth_consent_decision_time": None,
                  "username_screen_experience": "control",
                  "reduced_tos_test_group": "control",
                  "should_show_spi_before_conf": True,
                  "google_oauth_account": None,
                  "is_reg_request_from_ig_suma": False,
                  "is_igios_spc_reg": False,
                  "device_emails": None,
                  "is_toa_reg": False,
                  "is_threads_public": False,
                  "spc_import_flow": False,
                  "caa_play_integrity_attestation_result": None,
                  "flash_call_provider": None,
                  "name_prefill_variant": "control",
                  "spc_birthday_input": False,
                  "failed_birthday_year_count": None,
                  "user_presented_medium_source": None
              }),
              "flow_info": json.dumps({
                  "flow_name": "new_to_family_fb_default",
                  "flow_type": "ntf"
              }),
              "current_step": 2,
              "INTERNAL_INFRA_screen_id": "bloks.caa.reg.birthday"
          }),
          "client_input_params": json.dumps({
              "lois_settings": json.dumps({
                  "lois_token": "",
                  "lara_override": ""
              })
          })
      })
    }
  
  def data_birthday(self):
    birday = datetime.strptime(self.tgl, "%d-%m-%Y")
    self.times = int(birday.timestamp())
    return {
      "params": json.dumps({
        "server_params": json.dumps({
          "reg_info": json.dumps({
            "first_name": "{}".format(self.firstnama),
            "last_name": "{}".format(self.lastnama),
            "full_name": "{}".format(self.firstnama),
            "contactpoint": None,
            "ar_contactpoint": None,
            "contactpoint_type": None,
            "is_using_unified_cp": None,
            "unified_cp_screen_variant": None,
            "is_cp_auto_confirmed": False,
            "is_cp_auto_confirmable": False,
            "confirmation_code": None,
            "birthday": None,
            "did_use_age": False,
            "gender": None,
            "use_custom_gender": False,
            "custom_gender": None,
            "encrypted_password": None,
            "username": None,
            "username_prefill": None,
            "fb_conf_source": None,
            "device_id": None,
            "ig4a_qe_device_id": None,
            "family_device_id": None,
            "nta_eligibility_reason": None,
            "ig_nta_test_group": None,
            "user_id": None,
            "safetynet_token": None,
            "safetynet_response": None,
            "machine_id": None,
            "profile_photo": None,
            "profile_photo_id": None,
            "profile_photo_upload_id": None,
            "avatar": None,
            "email_oauth_token_no_contact_perm": None,
            "email_oauth_token": None,
            "email_oauth_tokens": None,
            "should_skip_two_step_conf": None,
            "openid_tokens_for_testing": None,
            "encrypted_msisdn": None,
            "encrypted_msisdn_for_safetynet": None,
            "cached_headers_safetynet_info": None,
            "should_skip_headers_safetynet": None,
            "headers_last_infra_flow_id": None,
            "headers_last_infra_flow_id_safetynet": None,
            "headers_flow_id": None,
            "was_headers_prefill_available": None,
            "sso_enabled": None,
            "existing_accounts": None,
            "used_ig_birthday": None,
            "sync_info": None,
            "create_new_to_app_account": None,
            "skip_session_info": None,
            "ck_error": None,
            "ck_id": None,
            "ck_nonce": None,
            "should_save_password": None,
            "horizon_synced_username": None,
            "fb_access_token": None,
            "horizon_synced_profile_pic": None,
            "is_identity_synced": False,
            "is_msplit_reg": None,
            "user_id_of_msplit_creator": None,
            "dma_data_combination_consent_given": None,
            "xapp_accounts": None,
            "fb_device_id": None,
            "fb_machine_id": None,
            "ig_device_id": None,
            "ig_machine_id": None,
            "should_skip_nta_upsell": None,
            "big_blue_token": None,
            "skip_sync_step_nta": None,
            "caa_reg_flow_source": None,
            "ig_authorization_token": None,
            "full_sheet_flow": False,
            "crypted_user_id": None,
            "is_caa_perf_enabled": False,
            "is_preform": True,
            "ignore_suma_check": False,
            "ignore_existing_login": False,
            "ignore_existing_login_from_suma": False,
            "ignore_existing_login_after_errors": False,
            "suggested_first_name": None,
            "suggested_last_name": None,
            "suggested_full_name": None,
            "replace_id_sync_variant": None,
            "is_redirect_from_nta_replace_id_sync_variant": False,
            "frl_authorization_token": None,
            "post_form_errors": None,
            "skip_step_without_errors": False,
            "existing_account_exact_match_checked": False,
            "existing_account_fuzzy_match_checked": False,
            "email_oauth_exists": False,
            "confirmation_code_send_error": None,
            "is_too_young": False,
            "source_account_type": None,
            "whatsapp_installed_on_client": False,
            "confirmation_medium": None,
            "source_credentials_type": None,
            "source_cuid": None,
            "source_account_reg_info": None,
            "soap_creation_source": None,
            "source_account_type_to_reg_info": None,
            "registration_flow_id": "",
            "should_skip_youth_tos": False,
            "is_youth_regulation_flow_complete": False,
            "is_on_cold_start": False,
            "email_prefilled": False,
            "cp_confirmed_by_auto_conf": False,
            "auto_conf_info": None,
            "in_sowa_experiment": False,
            "youth_regulation_config": None,
            "conf_allow_back_nav_after_change_cp": None,
            "conf_bouncing_cliff_screen_type": None,
            "conf_show_bouncing_cliff": None,
            "eligible_to_flash_call_in_ig4a": False,
            "flash_call_permissions_status": None,
            "attestation_result": None,
            "request_data_and_challenge_nonce_string": None,
            "confirmed_cp_and_code": None,
            "notification_callback_id": None,
            "reg_suma_state": 0,
            "is_msplit_neutral_choice": False,
            "msg_previous_cp": None,
            "ntp_import_source_info": None,
            "youth_consent_decision_time": None,
            "username_screen_experience": "control",
            "reduced_tos_test_group": "control",
            "should_show_spi_before_conf": True,
            "google_oauth_account": None,
            "is_reg_request_from_ig_suma": False,
            "is_igios_spc_reg": False,
            "device_emails": None,
            "is_toa_reg": False,
            "is_threads_public": False,
            "spc_import_flow": False,
            "caa_play_integrity_attestation_result": None,
            "flash_call_provider": None,
            "name_prefill_variant": "control",
            "spc_birthday_input": False,
            "failed_birthday_year_count": None,
            "user_presented_medium_source": None
          }),
          "flow_info": json.dumps({
            "flow_name": "new_to_family_fb_default",
            "flow_type": "ntf"
          }),
          "current_step": 2,
          "INTERNAL__latency_qpl_marker_id": 36707139,
          "INTERNAL__latency_qpl_instance_id": "2554918600113",
          "device_id": None,
          "family_device_id": None,
          "waterfall_id": "{}".format(self.uid1),
          "offline_experiment_group": None,
          "layered_homepage_experiment_group": None,
          "is_platform_login": 0,
          "is_from_logged_in_switcher": 0,
          "is_from_logged_out": 0,
          "access_flow_version": "F2_FLOW",
          "INTERNAL_INFRA_THEME": "harm_f"
        }),
        "client_input_params": json.dumps({
          "birthday_timestamp": self.times,
          "should_skip_youth_tos": 0,
          "is_youth_regulation_flow_complete": 0,
          "lois_settings": json.dumps({
            "lois_token": "",
            "lara_override": ""
          })
        })
      })
    }
  def response_birthday(self):
    return {
      "params": json.dumps({
          "server_params": json.dumps({
              "waterfall_id": "{}".format(self.uid1),
              "is_platform_login": 0,
              "is_from_logged_out": 0,
              "access_flow_version": "F2_FLOW",
              "reg_info": json.dumps({
                  "first_name": "{}".format(self.firstnama),
                  "last_name": "{}".format(self.lastnama),
                  "full_name": "{}".format(self.firstnama),
                  "contactpoint": None,
                  "ar_contactpoint": None,
                  "contactpoint_type": None,
                  "is_using_unified_cp": None,
                  "unified_cp_screen_variant": None,
                  "is_cp_auto_confirmed": False,
                  "is_cp_auto_confirmable": False,
                  "confirmation_code": None,
                  "birthday": "{}".format(self.tgl),
                  "did_use_age": False,
                  "gender": None,
                  "use_custom_gender": False,
                  "custom_gender": None,
                  "encrypted_password": None,
                  "username": None,
                  "username_prefill": None,
                  "fb_conf_source": None,
                  "device_id": None,
                  "ig4a_qe_device_id": None,
                  "family_device_id": None,
                  "nta_eligibility_reason": None,
                  "ig_nta_test_group": None,
                  "user_id": None,
                  "safetynet_token": None,
                  "safetynet_response": None,
                  "machine_id": None,
                  "profile_photo": None,
                  "profile_photo_id": None,
                  "profile_photo_upload_id": None,
                  "avatar": None,
                  "email_oauth_token_no_contact_perm": None,
                  "email_oauth_token": None,
                  "email_oauth_tokens": None,
                  "should_skip_two_step_conf": None,
                  "openid_tokens_for_testing": None,
                  "encrypted_msisdn": None,
                  "encrypted_msisdn_for_safetynet": None,
                  "cached_headers_safetynet_info": None,
                  "should_skip_headers_safetynet": None,
                  "headers_last_infra_flow_id": None,
                  "headers_last_infra_flow_id_safetynet": None,
                  "headers_flow_id": None,
                  "was_headers_prefill_available": None,
                  "sso_enabled": None,
                  "existing_accounts": None,
                  "used_ig_birthday": None,
                  "sync_info": None,
                  "create_new_to_app_account": None,
                  "skip_session_info": None,
                  "ck_error": None,
                  "ck_id": None,
                  "ck_nonce": None,
                  "should_save_password": None,
                  "horizon_synced_username": None,
                  "fb_access_token": None,
                  "horizon_synced_profile_pic": None,
                  "is_identity_synced": False,
                  "is_msplit_reg": None,
                  "user_id_of_msplit_creator": None,
                  "dma_data_combination_consent_given": None,
                  "xapp_accounts": None,
                  "fb_device_id": None,
                  "fb_machine_id": None,
                  "ig_device_id": None,
                  "ig_machine_id": None,
                  "should_skip_nta_upsell": None,
                  "big_blue_token": None,
                  "skip_sync_step_nta": None,
                  "caa_reg_flow_source": None,
                  "ig_authorization_token": None,
                  "full_sheet_flow": False,
                  "crypted_user_id": None,
                  "is_caa_perf_enabled": False,
                  "is_preform": True,
                  "ignore_suma_check": False,
                  "ignore_existing_login": False,
                  "ignore_existing_login_from_suma": False,
                  "ignore_existing_login_after_errors": False,
                  "suggested_first_name": None,
                  "suggested_last_name": None,
                  "suggested_full_name": None,
                  "replace_id_sync_variant": None,
                  "is_redirect_from_nta_replace_id_sync_variant": False,
                  "frl_authorization_token": None,
                  "post_form_errors": None,
                  "skip_step_without_errors": False,
                  "existing_account_exact_match_checked": False,
                  "existing_account_fuzzy_match_checked": False,
                  "email_oauth_exists": False,
                  "confirmation_code_send_error": None,
                  "is_too_young": False,
                  "source_account_type": None,
                  "whatsapp_installed_on_client": False,
                  "confirmation_medium": None,
                  "source_credentials_type": None,
                  "source_cuid": None,
                  "source_account_reg_info": None,
                  "soap_creation_source": None,
                  "source_account_type_to_reg_info": None,
                  "registration_flow_id": "",
                  "should_skip_youth_tos": False,
                  "is_youth_regulation_flow_complete": False,
                  "is_on_cold_start": False,
                  "email_prefilled": False,
                  "cp_confirmed_by_auto_conf": False,
                  "auto_conf_info": None,
                  "in_sowa_experiment": False,
                  "youth_regulation_config": None,
                  "conf_allow_back_nav_after_change_cp": None,
                  "conf_bouncing_cliff_screen_type": None,
                  "conf_show_bouncing_cliff": None,
                  "eligible_to_flash_call_in_ig4a": False,
                  "flash_call_permissions_status": None,
                  "attestation_result": None,
                  "request_data_and_challenge_nonce_string": None,
                  "confirmed_cp_and_code": None,
                  "notification_callback_id": None,
                  "reg_suma_state": 0,
                  "is_msplit_neutral_choice": False,
                  "msg_previous_cp": None,
                  "ntp_import_source_info": None,
                  "youth_consent_decision_time": None,
                  "username_screen_experience": "control",
                  "reduced_tos_test_group": "control",
                  "should_show_spi_before_conf": True,
                  "google_oauth_account": None,
                  "is_reg_request_from_ig_suma": False,
                  "is_igios_spc_reg": False,
                  "device_emails": None,
                  "is_toa_reg": False,
                  "is_threads_public": False,
                  "spc_import_flow": False,
                  "caa_play_integrity_attestation_result": None,
                  "flash_call_provider": None,
                  "name_prefill_variant": "control",
                  "spc_birthday_input": False,
                  "failed_birthday_year_count": None,
                  "user_presented_medium_source": None
              }),
              "flow_info": json.dumps({
                  "flow_name": "new_to_family_fb_default",
                  "flow_type": "ntf"
              }),
              "current_step": 3,
              "INTERNAL_INFRA_screen_id": "fhbht:21"
          }),
          "client_input_params": json.dumps({
              "lois_settings": json.dumps({
                  "lois_token": "",
                  "lara_override": ""
              })
          })
      })
    }
  def data_gender(self):
    return {
      "params": json.dumps({
        "server_params": json.dumps({
          "reg_info": json.dumps({
            "first_name": "{}".format(self.firstnama),
            "last_name": "{}".format(self.lastnama),
            "full_name": "{}".format(self.firstnama),
            "contactpoint": None,
            "ar_contactpoint": None,
            "contactpoint_type": None,
            "is_using_unified_cp": None,
            "unified_cp_screen_variant": None,
            "is_cp_auto_confirmed": False,
            "is_cp_auto_confirmable": False,
            "confirmation_code": None,
            "birthday": "{}".format(self.tgl),
            "did_use_age": False,
            "gender": None,
            "use_custom_gender": False,
            "custom_gender": None,
            "encrypted_password": None,
            "username": None,
            "username_prefill": None,
            "fb_conf_source": None,
            "device_id": None,
            "ig4a_qe_device_id": None,
            "family_device_id": None,
            "nta_eligibility_reason": None,
            "ig_nta_test_group": None,
            "user_id": None,
            "safetynet_token": None,
            "safetynet_response": None,
            "machine_id": None,
            "profile_photo": None,
            "profile_photo_id": None,
            "profile_photo_upload_id": None,
            "avatar": None,
            "email_oauth_token_no_contact_perm": None,
            "email_oauth_token": None,
            "email_oauth_tokens": None,
            "should_skip_two_step_conf": None,
            "openid_tokens_for_testing": None,
            "encrypted_msisdn": None,
            "encrypted_msisdn_for_safetynet": None,
            "cached_headers_safetynet_info": None,
            "should_skip_headers_safetynet": None,
            "headers_last_infra_flow_id": None,
            "headers_last_infra_flow_id_safetynet": None,
            "headers_flow_id": None,
            "was_headers_prefill_available": None,
            "sso_enabled": None,
            "existing_accounts": None,
            "used_ig_birthday": None,
            "sync_info": None,
            "create_new_to_app_account": None,
            "skip_session_info": None,
            "ck_error": None,
            "ck_id": None,
            "ck_nonce": None,
            "should_save_password": None,
            "horizon_synced_username": None,
            "fb_access_token": None,
            "horizon_synced_profile_pic": None,
            "is_identity_synced": False,
            "is_msplit_reg": None,
            "user_id_of_msplit_creator": None,
            "dma_data_combination_consent_given": None,
            "xapp_accounts": None,
            "fb_device_id": None,
            "fb_machine_id": None,
            "ig_device_id": None,
            "ig_machine_id": None,
            "should_skip_nta_upsell": None,
            "big_blue_token": None,
            "skip_sync_step_nta": None,
            "caa_reg_flow_source": None,
            "ig_authorization_token": None,
            "full_sheet_flow": False,
            "crypted_user_id": None,
            "is_caa_perf_enabled": False,
            "is_preform": True,
            "ignore_suma_check": False,
            "ignore_existing_login": False,
            "ignore_existing_login_from_suma": False,
            "ignore_existing_login_after_errors": False,
            "suggested_first_name": None,
            "suggested_last_name": None,
            "suggested_full_name": None,
            "replace_id_sync_variant": None,
            "is_redirect_from_nta_replace_id_sync_variant": False,
            "frl_authorization_token": None,
            "post_form_errors": None,
            "skip_step_without_errors": False,
            "existing_account_exact_match_checked": False,
            "existing_account_fuzzy_match_checked": False,
            "email_oauth_exists": False,
            "confirmation_code_send_error": None,
            "is_too_young": False,
            "source_account_type": None,
            "whatsapp_installed_on_client": False,
            "confirmation_medium": None,
            "source_credentials_type": None,
            "source_cuid": None,
            "source_account_reg_info": None,
            "soap_creation_source": None,
            "source_account_type_to_reg_info": None,
            "registration_flow_id": "",
            "should_skip_youth_tos": False,
            "is_youth_regulation_flow_complete": False,
            "is_on_cold_start": False,
            "email_prefilled": False,
            "cp_confirmed_by_auto_conf": False,
            "auto_conf_info": None,
            "in_sowa_experiment": False,
            "youth_regulation_config": None,
            "conf_allow_back_nav_after_change_cp": None,
            "conf_bouncing_cliff_screen_type": None,
            "conf_show_bouncing_cliff": None,
            "eligible_to_flash_call_in_ig4a": False,
            "flash_call_permissions_status": None,
            "attestation_result": None,
            "request_data_and_challenge_nonce_string": None,
            "confirmed_cp_and_code": None,
            "notification_callback_id": None,
            "reg_suma_state": 0,
            "is_msplit_neutral_choice": False,
            "msg_previous_cp": None,
            "ntp_import_source_info": None,
            "youth_consent_decision_time": None,
            "username_screen_experience": "control",
            "reduced_tos_test_group": "control",
            "should_show_spi_before_conf": True,
            "google_oauth_account": None,
            "is_reg_request_from_ig_suma": False,
            "is_igios_spc_reg": False,
            "device_emails": None,
            "is_toa_reg": False,
            "is_threads_public": False,
            "spc_import_flow": False,
            "caa_play_integrity_attestation_result": None,
            "flash_call_provider": None,
            "name_prefill_variant": "control",
            "spc_birthday_input": False,
            "failed_birthday_year_count": None,
            "user_presented_medium_source": None
          }),
          "flow_info": json.dumps({
            "flow_name": "new_to_family_fb_default",
            "flow_type": "ntf"
          }),
          "current_step": 3,
          "INTERNAL__latency_qpl_marker_id": 36707139,
          "INTERNAL__latency_qpl_instance_id": "2602202300118",
          "device_id": None,
          "family_device_id": None,
          "waterfall_id": "{}".format(self.uid1),
          "offline_experiment_group": None,
          "layered_homepage_experiment_group": None,
          "is_platform_login": 0,
          "is_from_logged_in_switcher": 0,
          "is_from_logged_out": 0,
          "access_flow_version": "F2_FLOW",
          "INTERNAL_INFRA_THEME": "harm_f"
        }),
        "client_input_params": json.dumps({
          "gender": 1,
          "pronoun": 0,
          "custom_gender": "",
          "device_phone_numbers": [],
          "lois_settings": json.dumps({
            "lois_token": "",
            "lara_override": ""
          })
        })
      })
    }
    
  def response_gender(self):
    return{
      "params": json.dumps({
        "server_params": json.dumps({
          "waterfall_id": "{}".format(self.uid1),
          "is_platform_login": 0,
          "is_from_logged_out": 0,
          "access_flow_version": "F2_FLOW",
          "root_screen_id": "bloks.caa.reg.contactpoint_phone",
          "reg_info": json.dumps({
            "first_name": "{}".format(self.firstnama),
            "last_name": "{}".format(self.lastnama),
            "full_name": "{}".format(self.firstnama),
            "contactpoint": None,
            "ar_contactpoint": None,
            "contactpoint_type": None,
            "is_using_unified_cp": None,
            "unified_cp_screen_variant": None,
            "is_cp_auto_confirmed": False,
            "is_cp_auto_confirmable": False,
            "confirmation_code": None,
            "birthday": "{}".format(self.tgl),
            "did_use_age": False,
            "gender": self.gender,
            "use_custom_gender": False,
            "custom_gender": None,
            "encrypted_password": None,
            "username": None,
            "username_prefill": None,
            "fb_conf_source": None,
            "device_id": None,
            "ig4a_qe_device_id": None,
            "family_device_id": None,
            "nta_eligibility_reason": None,
            "ig_nta_test_group": None,
            "user_id": None,
            "safetynet_token": None,
            "safetynet_response": None,
            "machine_id": None,
            "profile_photo": None,
            "profile_photo_id": None,
            "profile_photo_upload_id": None,
            "avatar": None,
            "email_oauth_token_no_contact_perm": None,
            "email_oauth_token": None,
            "email_oauth_tokens": None,
            "should_skip_two_step_conf": None,
            "openid_tokens_for_testing": None,
            "encrypted_msisdn": None,
            "encrypted_msisdn_for_safetynet": None,
            "cached_headers_safetynet_info": None,
            "should_skip_headers_safetynet": None,
            "headers_last_infra_flow_id": None,
            "headers_last_infra_flow_id_safetynet": None,
            "headers_flow_id": None,
            "was_headers_prefill_available": None,
            "sso_enabled": None,
            "existing_accounts": None,
            "used_ig_birthday": None,
            "sync_info": None,
            "create_new_to_app_account": None,
            "skip_session_info": None,
            "ck_error": None,
            "ck_id": None,
            "ck_nonce": None,
            "should_save_password": None,
            "horizon_synced_username": None,
            "fb_access_token": None,
            "horizon_synced_profile_pic": None,
            "is_identity_synced": False,
            "is_msplit_reg": None,
            "user_id_of_msplit_creator": None,
            "dma_data_combination_consent_given": None,
            "xapp_accounts": None,
            "fb_device_id": None,
            "fb_machine_id": None,
            "ig_device_id": None,
            "ig_machine_id": None,
            "should_skip_nta_upsell": None,
            "big_blue_token": None,
            "skip_sync_step_nta": None,
            "caa_reg_flow_source": None,
            "ig_authorization_token": None,
            "full_sheet_flow": False,
            "crypted_user_id": None,
            "is_caa_perf_enabled": False,
            "is_preform": True,
            "ignore_suma_check": False,
            "ignore_existing_login": False,
            "ignore_existing_login_from_suma": False,
            "ignore_existing_login_after_errors": False,
            "suggested_first_name": None,
            "suggested_last_name": None,
            "suggested_full_name": None,
            "replace_id_sync_variant": None,
            "is_redirect_from_nta_replace_id_sync_variant": False,
            "frl_authorization_token": None,
            "post_form_errors": None,
            "skip_step_without_errors": False,
            "existing_account_exact_match_checked": False,
            "existing_account_fuzzy_match_checked": False,
            "email_oauth_exists": False,
            "confirmation_code_send_error": None,
            "is_too_young": False,
            "source_account_type": None,
            "whatsapp_installed_on_client": False,
            "confirmation_medium": None,
            "source_credentials_type": None,
            "source_cuid": None,
            "source_account_reg_info": None,
            "soap_creation_source": None,
            "source_account_type_to_reg_info": None,
            "registration_flow_id": "",
            "should_skip_youth_tos": False,
            "is_youth_regulation_flow_complete": False,
            "is_on_cold_start": False,
            "email_prefilled": False,
            "cp_confirmed_by_auto_conf": False,
            "auto_conf_info": None,
            "in_sowa_experiment": False,
            "youth_regulation_config": None,
            "conf_allow_back_nav_after_change_cp": None,
            "conf_bouncing_cliff_screen_type": None,
            "conf_show_bouncing_cliff": None,
            "eligible_to_flash_call_in_ig4a": False,
            "flash_call_permissions_status": None,
            "attestation_result": None,
            "request_data_and_challenge_nonce_string": None,
            "confirmed_cp_and_code": None,
            "notification_callback_id": None,
            "reg_suma_state": 0,
            "is_msplit_neutral_choice": False,
            "msg_previous_cp": None,
            "ntp_import_source_info": None,
            "youth_consent_decision_time": None,
            "username_screen_experience": "control",
            "reduced_tos_test_group": "control",
            "should_show_spi_before_conf": True,
            "google_oauth_account": None,
            "is_reg_request_from_ig_suma": False,
            "is_igios_spc_reg": False,
            "device_emails": None,
            "is_toa_reg": False,
            "is_threads_public": False,
            "spc_import_flow": False,
            "caa_play_integrity_attestation_result": None,
            "flash_call_provider": None,
            "name_prefill_variant": "control",
            "spc_birthday_input": False,
            "failed_birthday_year_count": None,
            "user_presented_medium_source": None
          }),
          "flow_info": json.dumps({
            "flow_name": "new_to_family_fb_default",
            "flow_type": "ntf"
          }),
          "current_step": 4,
          "INTERNAL_INFRA_screen_id": "CAA_REG_CONTACT_POINT_EMAIL"
        }),
        "client_input_params": json.dumps({
          "lois_settings": json.dumps({
            "lois_token": "",
            "lara_override": ""
          })
        })
      })
    }
    
  def data_email(self, mail):
    self.mail = mail
    return {
      "params": json.dumps({
          "server_params": json.dumps({
              "event_request_id": "{}".format(self.uid),
              "cp_funnel": 0,
              "cp_source": 0,
              "text_input_id": "2669779800065",
              "reg_info": json.dumps({
                  "first_name": "{}".format(self.firstnama),
                  "last_name": "{}".format(self.lastnama),
                  "full_name": "{}".format(self.firstnama),
                  "contactpoint": None,
                  "ar_contactpoint": None,
                  "contactpoint_type": None,
                  "is_using_unified_cp": None,
                  "unified_cp_screen_variant": None,
                  "is_cp_auto_confirmed": False,
                  "is_cp_auto_confirmable": False,
                  "confirmation_code": None,
                  "birthday": "{}".format(self.tgl),
                  "did_use_age": False,
                  "gender": self.gender,
                  "use_custom_gender": False,
                  "custom_gender": None,
                  "encrypted_password": None,
                  "username": None,
                  "username_prefill": None,
                  "fb_conf_source": None,
                  "device_id": None,
                  "ig4a_qe_device_id": None,
                  "family_device_id": None,
                  "nta_eligibility_reason": None,
                  "ig_nta_test_group": None,
                  "user_id": None,
                  "safetynet_token": None,
                  "safetynet_response": None,
                  "machine_id": None,
                  "profile_photo": None,
                  "profile_photo_id": None,
                  "profile_photo_upload_id": None,
                  "avatar": None,
                  "email_oauth_token_no_contact_perm": None,
                  "email_oauth_token": None,
                  "email_oauth_tokens": None,
                  "should_skip_two_step_conf": None,
                  "openid_tokens_for_testing": None,
                  "encrypted_msisdn": None,
                  "encrypted_msisdn_for_safetynet": None,
                  "cached_headers_safetynet_info": None,
                  "should_skip_headers_safetynet": None,
                  "headers_last_infra_flow_id": None,
                  "headers_last_infra_flow_id_safetynet": None,
                  "headers_flow_id": None,
                  "was_headers_prefill_available": None,
                  "sso_enabled": None,
                  "existing_accounts": None,
                  "used_ig_birthday": None,
                  "sync_info": None,
                  "create_new_to_app_account": None,
                  "skip_session_info": None,
                  "ck_error": None,
                  "ck_id": None,
                  "ck_nonce": None,
                  "should_save_password": None,
                  "horizon_synced_username": None,
                  "fb_access_token": None,
                  "horizon_synced_profile_pic": None,
                  "is_identity_synced": False,
                  "is_msplit_reg": None,
                  "user_id_of_msplit_creator": None,
                  "dma_data_combination_consent_given": None,
                  "xapp_accounts": None,
                  "fb_device_id": None,
                  "fb_machine_id": None,
                  "ig_device_id": None,
                  "ig_machine_id": None,
                  "should_skip_nta_upsell": None,
                  "big_blue_token": None,
                  "skip_sync_step_nta": None,
                  "caa_reg_flow_source": None,
                  "ig_authorization_token": None,
                  "full_sheet_flow": False,
                  "crypted_user_id": None,
                  "is_caa_perf_enabled": False,
                  "is_preform": True,
                  "ignore_suma_check": False,
                  "ignore_existing_login": False,
                  "ignore_existing_login_from_suma": False,
                  "ignore_existing_login_after_errors": False,
                  "suggested_first_name": None,
                  "suggested_last_name": None,
                  "suggested_full_name": None,
                  "replace_id_sync_variant": None,
                  "is_redirect_from_nta_replace_id_sync_variant": False,
                  "frl_authorization_token": None,
                  "post_form_errors": None,
                  "skip_step_without_errors": False,
                  "existing_account_exact_match_checked": False,
                  "existing_account_fuzzy_match_checked": False,
                  "email_oauth_exists": False,
                  "confirmation_code_send_error": None,
                  "is_too_young": False,
                  "source_account_type": None,
                  "whatsapp_installed_on_client": False,
                  "confirmation_medium": None,
                  "source_credentials_type": None,
                  "source_cuid": None,
                  "source_account_reg_info": None,
                  "soap_creation_source": None,
                  "source_account_type_to_reg_info": None,
                  "registration_flow_id": "",
                  "should_skip_youth_tos": False,
                  "is_youth_regulation_flow_complete": False,
                  "is_on_cold_start": False,
                  "email_prefilled": False,
                  "cp_confirmed_by_auto_conf": False,
                  "auto_conf_info": None,
                  "in_sowa_experiment": False,
                  "youth_regulation_config": None,
                  "conf_allow_back_nav_after_change_cp": None,
                  "conf_bouncing_cliff_screen_type": None,
                  "conf_show_bouncing_cliff": None,
                  "eligible_to_flash_call_in_ig4a": False,
                  "flash_call_permissions_status": None,
                  "attestation_result": None,
                  "request_data_and_challenge_nonce_string": None,
                  "confirmed_cp_and_code": None,
                  "notification_callback_id": None,
                  "reg_suma_state": 0,
                  "is_msplit_neutral_choice": False,
                  "msg_previous_cp": None,
                  "ntp_import_source_info": None,
                  "youth_consent_decision_time": None,
                  "username_screen_experience": "control",
                  "reduced_tos_test_group": "control",
                  "should_show_spi_before_conf": True,
                  "google_oauth_account": None,
                  "is_reg_request_from_ig_suma": False,
                  "is_igios_spc_reg": False,
                  "device_emails": None,
                  "is_toa_reg": False,
                  "is_threads_public": False,
                  "spc_import_flow": False,
                  "caa_play_integrity_attestation_result": None,
                  "flash_call_provider": None,
                  "name_prefill_variant": "control",
                  "spc_birthday_input": False,
                  "failed_birthday_year_count": None,
                  "user_presented_medium_source": None
              }),
              "flow_info": json.dumps({
                  "flow_name": "new_to_family_fb_default",
                  "flow_type": "ntf"
              }),
              "current_step": 4,
              "INTERNAL__latency_qpl_marker_id": 36707139,
              "INTERNAL__latency_qpl_instance_id": "2669779800099",
              "device_id": None,
              "family_device_id": None,
              "waterfall_id": "{}".format(self.uid1),
              "offline_experiment_group": None,
              "layered_homepage_experiment_group": None,
              "is_platform_login": 0,
              "is_from_logged_in_switcher": 0,
              "is_from_logged_out": 0,
              "access_flow_version": "F2_FLOW",
              "INTERNAL_INFRA_THEME": "harm_f"
          }),
          "client_input_params": json.dumps({
              "device_id": "",
              "family_device_id": "",
              "email": "{}".format(self.mail),
              "email_prefilled": 0,
              "accounts_list": [],
              "fb_ig_device_id": [],
              "confirmed_cp_and_code": {},
              "is_from_device_emails": 0,
              "msg_previous_cp": "",
              "switch_cp_first_time_loading": 1,
              "switch_cp_have_seen_suma": 0,
              "lois_settings": json.dumps({
                  "lois_token": "",
                  "lara_override": ""
              })
          })
      })
    }
  
  def response_email(self,mail):
    self.mail = mail
    return {
      "params": json.dumps({
          "server_params": json.dumps({
              "waterfall_id": "{}".format(self.uid1),
              "is_platform_login": 0,
              "is_from_logged_out": 0,
              "access_flow_version": "F2_FLOW",
              "reg_info": json.dumps({
                  "first_name": "{}".format(self.firstnama),
                  "last_name": "{}".format(self.lastnama),
                  "full_name": "{}".format(self.firstnama),
                  "contactpoint": "{}".format(self.mail),
                  "ar_contactpoint": None,
                  "contactpoint_type": "email",
                  "is_using_unified_cp": False,
                  "unified_cp_screen_variant": None,
                  "is_cp_auto_confirmed": False,
                  "is_cp_auto_confirmable": False,
                  "confirmation_code": None,
                  "birthday": "{}".format(self.tgl),
                  "did_use_age": False,
                  "gender": self.gender,
                  "use_custom_gender": False,
                  "custom_gender": None,
                  "encrypted_password": None,
                  "username": None,
                  "username_prefill": None,
                  "fb_conf_source": None,
                  "device_id": None,
                  "ig4a_qe_device_id": None,
                  "family_device_id": None,
                  "nta_eligibility_reason": None,
                  "ig_nta_test_group": None,
                  "user_id": None,
                  "safetynet_token": None,
                  "safetynet_response": None,
                  "machine_id": None,
                  "profile_photo": None,
                  "profile_photo_id": None,
                  "profile_photo_upload_id": None,
                  "avatar": None,
                  "email_oauth_token_no_contact_perm": None,
                  "email_oauth_token": None,
                  "email_oauth_tokens": None,
                  "should_skip_two_step_conf": None,
                  "openid_tokens_for_testing": None,
                  "encrypted_msisdn": None,
                  "encrypted_msisdn_for_safetynet": None,
                  "cached_headers_safetynet_info": None,
                  "should_skip_headers_safetynet": None,
                  "headers_last_infra_flow_id": None,
                  "headers_last_infra_flow_id_safetynet": None,
                  "headers_flow_id": None,
                  "was_headers_prefill_available": None,
                  "sso_enabled": None,
                  "existing_accounts": None,
                  "used_ig_birthday": None,
                  "sync_info": None,
                  "create_new_to_app_account": None,
                  "skip_session_info": None,
                  "ck_error": None,
                  "ck_id": None,
                  "ck_nonce": None,
                  "should_save_password": None,
                  "horizon_synced_username": None,
                  "fb_access_token": None,
                  "horizon_synced_profile_pic": None,
                  "is_identity_synced": False,
                  "is_msplit_reg": None,
                  "user_id_of_msplit_creator": None,
                  "dma_data_combination_consent_given": None,
                  "xapp_accounts": None,
                  "fb_device_id": None,
                  "fb_machine_id": None,
                  "ig_device_id": None,
                  "ig_machine_id": None,
                  "should_skip_nta_upsell": None,
                  "big_blue_token": None,
                  "skip_sync_step_nta": None,
                  "caa_reg_flow_source": None,
                  "ig_authorization_token": None,
                  "full_sheet_flow": False,
                  "crypted_user_id": None,
                  "is_caa_perf_enabled": False,
                  "is_preform": True,
                  "ignore_suma_check": False,
                  "ignore_existing_login": False,
                  "ignore_existing_login_from_suma": False,
                  "ignore_existing_login_after_errors": False,
                  "suggested_first_name": None,
                  "suggested_last_name": None,
                  "suggested_full_name": None,
                  "replace_id_sync_variant": None,
                  "is_redirect_from_nta_replace_id_sync_variant": False,
                  "frl_authorization_token": None,
                  "post_form_errors": None,
                  "skip_step_without_errors": False,
                  "existing_account_exact_match_checked": False,
                  "existing_account_fuzzy_match_checked": False,
                  "email_oauth_exists": False,
                  "confirmation_code_send_error": None,
                  "is_too_young": False,
                  "source_account_type": None,
                  "whatsapp_installed_on_client": False,
                  "confirmation_medium": None,
                  "source_credentials_type": None,
                  "source_cuid": None,
                  "source_account_reg_info": None,
                  "soap_creation_source": None,
                  "source_account_type_to_reg_info": None,
                  "registration_flow_id": "",
                  "should_skip_youth_tos": False,
                  "is_youth_regulation_flow_complete": False,
                  "is_on_cold_start": False,
                  "email_prefilled": False,
                  "cp_confirmed_by_auto_conf": False,
                  "auto_conf_info": None,
                  "in_sowa_experiment": False,
                  "youth_regulation_config": None,
                  "conf_allow_back_nav_after_change_cp": None,
                  "conf_bouncing_cliff_screen_type": None,
                  "conf_show_bouncing_cliff": None,
                  "eligible_to_flash_call_in_ig4a": False,
                  "flash_call_permissions_status": None,
                  "attestation_result": None,
                  "request_data_and_challenge_nonce_string": None,
                  "confirmed_cp_and_code": None,
                  "notification_callback_id": None,
                  "reg_suma_state": 0,
                  "is_msplit_neutral_choice": False,
                  "msg_previous_cp": None,
                  "ntp_import_source_info": None,
                  "youth_consent_decision_time": None,
                  "username_screen_experience": "control",
                  "reduced_tos_test_group": "control",
                  "should_show_spi_before_conf": True,
                  "google_oauth_account": None,
                  "is_reg_request_from_ig_suma": False,
                  "is_igios_spc_reg": False,
                  "device_emails": None,
                  "is_toa_reg": False,
                  "is_threads_public": False,
                  "spc_import_flow": False,
                  "caa_play_integrity_attestation_result": None,
                  "flash_call_provider": None,
                  "name_prefill_variant": "control",
                  "spc_birthday_input": False,
                  "failed_birthday_year_count": None,
                  "user_presented_medium_source": None
              }),
              "flow_info": json.dumps({
                  "flow_name": "new_to_family_fb_default",
                  "flow_type": "ntf"
              }),
              "current_step": 5,
              "INTERNAL_INFRA_screen_id": "CAA_REG_PASSWORD"
          }),
          "client_input_params": json.dumps({
              "lois_settings": json.dumps({
                  "lois_token": "",
                  "lara_override": ""
              })
          })
      })
    }
  
  def data_password(self, mail):
    self.mail = mail
    return {
      "params": json.dumps({
          "server_params": json.dumps({
              "event_request_id": "{}".format(self.uid),
              "reg_info": json.dumps({
                  "first_name": "{}".format(self.firstnama),
                  "last_name": "{}".format(self.lastnama),
                  "full_name": "{}".format(self.firstnama),
                  "contactpoint": "{}".format(self.mail),
                  "ar_contactpoint": None,
                  "contactpoint_type": "email",
                  "is_using_unified_cp": False,
                  "unified_cp_screen_variant": None,
                  "is_cp_auto_confirmed": False,
                  "is_cp_auto_confirmable": False,
                  "confirmation_code": None,
                  "birthday": "{}".format(self.tgl),
                  "did_use_age": False,
                  "gender": self.gender,
                  "use_custom_gender": False,
                  "custom_gender": None,
                  "encrypted_password": None,
                  "username": None,
                  "username_prefill": None,
                  "fb_conf_source": None,
                  "device_id": None,
                  "ig4a_qe_device_id": None,
                  "family_device_id": None,
                  "nta_eligibility_reason": None,
                  "ig_nta_test_group": None,
                  "user_id": None,
                  "safetynet_token": None,
                  "safetynet_response": None,
                  "machine_id": None,
                  "profile_photo": None,
                  "profile_photo_id": None,
                  "profile_photo_upload_id": None,
                  "avatar": None,
                  "email_oauth_token_no_contact_perm": None,
                  "email_oauth_token": None,
                  "email_oauth_tokens": None,
                  "should_skip_two_step_conf": None,
                  "openid_tokens_for_testing": None,
                  "encrypted_msisdn": None,
                  "encrypted_msisdn_for_safetynet": None,
                  "cached_headers_safetynet_info": None,
                  "should_skip_headers_safetynet": None,
                  "headers_last_infra_flow_id": None,
                  "headers_last_infra_flow_id_safetynet": None,
                  "headers_flow_id": None,
                  "was_headers_prefill_available": None,
                  "sso_enabled": None,
                  "existing_accounts": None,
                  "used_ig_birthday": None,
                  "sync_info": None,
                  "create_new_to_app_account": None,
                  "skip_session_info": None,
                  "ck_error": None,
                  "ck_id": None,
                  "ck_nonce": None,
                  "should_save_password": None,
                  "horizon_synced_username": None,
                  "fb_access_token": None,
                  "horizon_synced_profile_pic": None,
                  "is_identity_synced": False,
                  "is_msplit_reg": None,
                  "user_id_of_msplit_creator": None,
                  "dma_data_combination_consent_given": None,
                  "xapp_accounts": None,
                  "fb_device_id": None,
                  "fb_machine_id": None,
                  "ig_device_id": None,
                  "ig_machine_id": None,
                  "should_skip_nta_upsell": None,
                  "big_blue_token": None,
                  "skip_sync_step_nta": None,
                  "caa_reg_flow_source": None,
                  "ig_authorization_token": None,
                  "full_sheet_flow": False,
                  "crypted_user_id": None,
                  "is_caa_perf_enabled": False,
                  "is_preform": True,
                  "ignore_suma_check": False,
                  "ignore_existing_login": False,
                  "ignore_existing_login_from_suma": False,
                  "ignore_existing_login_after_errors": False,
                  "suggested_first_name": None,
                  "suggested_last_name": None,
                  "suggested_full_name": None,
                  "replace_id_sync_variant": None,
                  "is_redirect_from_nta_replace_id_sync_variant": False,
                  "frl_authorization_token": None,
                  "post_form_errors": None,
                  "skip_step_without_errors": False,
                  "existing_account_exact_match_checked": False,
                  "existing_account_fuzzy_match_checked": False,
                  "email_oauth_exists": False,
                  "confirmation_code_send_error": None,
                  "is_too_young": False,
                  "source_account_type": None,
                  "whatsapp_installed_on_client": False,
                  "confirmation_medium": None,
                  "source_credentials_type": None,
                  "source_cuid": None,
                  "source_account_reg_info": None,
                  "soap_creation_source": None,
                  "source_account_type_to_reg_info": None,
                  "registration_flow_id": "",
                  "should_skip_youth_tos": False,
                  "is_youth_regulation_flow_complete": False,
                  "is_on_cold_start": False,
                  "email_prefilled": False,
                  "cp_confirmed_by_auto_conf": False,
                  "auto_conf_info": None,
                  "in_sowa_experiment": False,
                  "youth_regulation_config": None,
                  "conf_allow_back_nav_after_change_cp": None,
                  "conf_bouncing_cliff_screen_type": None,
                  "conf_show_bouncing_cliff": None,
                  "eligible_to_flash_call_in_ig4a": False,
                  "flash_call_permissions_status": None,
                  "attestation_result": None,
                  "request_data_and_challenge_nonce_string": None,
                  "confirmed_cp_and_code": None,
                  "notification_callback_id": None,
                  "reg_suma_state": 0,
                  "is_msplit_neutral_choice": False,
                  "msg_previous_cp": None,
                  "ntp_import_source_info": None,
                  "youth_consent_decision_time": None,
                  "username_screen_experience": "control",
                  "reduced_tos_test_group": "control",
                  "should_show_spi_before_conf": True,
                  "google_oauth_account": None,
                  "is_reg_request_from_ig_suma": False,
                  "is_igios_spc_reg": False,
                  "device_emails": None,
                  "is_toa_reg": False,
                  "is_threads_public": False,
                  "spc_import_flow": False,
                  "caa_play_integrity_attestation_result": None,
                  "flash_call_provider": None,
                  "name_prefill_variant": "control",
                  "spc_birthday_input": False,
                  "failed_birthday_year_count": None,
                  "user_presented_medium_source": None
              }),
              "flow_info": json.dumps({
                  "flow_name": "new_to_family_fb_default",
                  "flow_type": "ntf"
              }),
              "current_step": 5,
              "INTERNAL__latency_qpl_marker_id": 36707139,
              "INTERNAL__latency_qpl_instance_id": "2841150900136",
              "device_id": None,
              "family_device_id": None,
              "waterfall_id": "{}".format(self.uid1),
              "offline_experiment_group": None,
              "layered_homepage_experiment_group": None,
              "is_platform_login": 0,
              "is_from_logged_in_switcher": 0,
              "is_from_logged_out": 0,
              "access_flow_version": "F2_FLOW",
              "INTERNAL_INFRA_THEME": "harm_f"
          }),
          "client_input_params": json.dumps({
              "machine_id": "",
              "encrypted_password": "#PWD_BROWSER:0:{}:{}".format(self.timer,self.pw),
              "safetynet_token": "",
              "safetynet_response": "",
              "email_oauth_token_map": {},
              "whatsapp_installed_on_client": 0,
              "encrypted_msisdn_for_safetynet": "",
              "headers_last_infra_flow_id_safetynet": "",
              "fb_ig_device_id": [],
              "caa_play_integrity_attestation_result": "",
              "lois_settings": json.dumps({
                  "lois_token": "",
                  "lara_override": ""
              })
          })
      })
    }
    
  def response_password(self,mail):
    self.mail = mail
    return {
      "params": json.dumps({
        "server_params": json.dumps({
          "waterfall_id": "{}".format(self.uid1),
          "is_platform_login": 0,
          "is_from_logged_out": 0,
          "access_flow_version": "F2_FLOW",
          "reg_info": json.dumps({
            "first_name": "{}".format(self.firstnama),
            "last_name": "{}".format(self.lastnama),
            "full_name": "{}".format(self.firstnama),
            "contactpoint": "{}".format(self.mail),
            "ar_contactpoint": None,
            "contactpoint_type": "email",
            "is_using_unified_cp": False,
            "unified_cp_screen_variant": None,
            "is_cp_auto_confirmed": False,
            "is_cp_auto_confirmable": False,
            "confirmation_code": None,
            "birthday": "{}".format(self.tgl),
            "did_use_age": False,
            "gender": self.gender,
            "use_custom_gender": False,
            "custom_gender": None,
            "encrypted_password": "#PWD_BROWSER:5:{}:{}".format(self.timer,self.pw),
            "username": None,
            "username_prefill": None,
            "fb_conf_source": None,
            "device_id": None,
            "ig4a_qe_device_id": None,
            "family_device_id": None,
            "nta_eligibility_reason": None,
            "ig_nta_test_group": None,
            "user_id": None,
            "safetynet_token": None,
            "safetynet_response": None,
            "machine_id": None,
            "profile_photo": None,
            "profile_photo_id": None,
            "profile_photo_upload_id": None,
            "avatar": None,
            "email_oauth_token_no_contact_perm": None,
            "email_oauth_token": None,
            "email_oauth_tokens": [],
            "should_skip_two_step_conf": None,
            "openid_tokens_for_testing": None,
            "encrypted_msisdn": None,
            "encrypted_msisdn_for_safetynet": None,
            "cached_headers_safetynet_info": None,
            "should_skip_headers_safetynet": None,
            "headers_last_infra_flow_id": None,
            "headers_last_infra_flow_id_safetynet": None,
            "headers_flow_id": None,
            "was_headers_prefill_available": None,
            "sso_enabled": None,
            "existing_accounts": None,
            "used_ig_birthday": None,
            "sync_info": None,
            "create_new_to_app_account": None,
            "skip_session_info": None,
            "ck_error": None,
            "ck_id": None,
            "ck_nonce": None,
            "should_save_password": None,
            "horizon_synced_username": None,
            "fb_access_token": None,
            "horizon_synced_profile_pic": None,
            "is_identity_synced": False,
            "is_msplit_reg": None,
            "user_id_of_msplit_creator": None,
            "dma_data_combination_consent_given": None,
            "xapp_accounts": None,
            "fb_device_id": None,
            "fb_machine_id": None,
            "ig_device_id": None,
            "ig_machine_id": None,
            "should_skip_nta_upsell": None,
            "big_blue_token": None,
            "skip_sync_step_nta": None,
            "caa_reg_flow_source": None,
            "ig_authorization_token": None,
            "full_sheet_flow": False,
            "crypted_user_id": None,
            "is_caa_perf_enabled": False,
            "is_preform": True,
            "ignore_suma_check": False,
            "ignore_existing_login": False,
            "ignore_existing_login_from_suma": False,
            "ignore_existing_login_after_errors": False,
            "suggested_first_name": None,
            "suggested_last_name": None,
            "suggested_full_name": None,
            "replace_id_sync_variant": None,
            "is_redirect_from_nta_replace_id_sync_variant": False,
            "frl_authorization_token": None,
            "post_form_errors": None,
            "skip_step_without_errors": False,
            "existing_account_exact_match_checked": False,
            "existing_account_fuzzy_match_checked": False,
            "email_oauth_exists": False,
            "confirmation_code_send_error": None,
            "is_too_young": False,
            "source_account_type": None,
            "whatsapp_installed_on_client": False,
            "confirmation_medium": None,
            "source_credentials_type": None,
            "source_cuid": None,
            "source_account_reg_info": None,
            "soap_creation_source": None,
            "source_account_type_to_reg_info": None,
            "registration_flow_id": "",
            "should_skip_youth_tos": False,
            "is_youth_regulation_flow_complete": False,
            "is_on_cold_start": False,
            "email_prefilled": False,
            "cp_confirmed_by_auto_conf": False,
            "auto_conf_info": None,
            "in_sowa_experiment": False,
            "youth_regulation_config": None,
            "conf_allow_back_nav_after_change_cp": None,
            "conf_bouncing_cliff_screen_type": None,
            "conf_show_bouncing_cliff": None,
            "eligible_to_flash_call_in_ig4a": False,
            "flash_call_permissions_status": None,
            "attestation_result": None,
            "request_data_and_challenge_nonce_string": None,
            "confirmed_cp_and_code": None,
            "notification_callback_id": None,
            "reg_suma_state": 0,
            "is_msplit_neutral_choice": False,
            "msg_previous_cp": None,
            "ntp_import_source_info": None,
            "youth_consent_decision_time": None,
            "username_screen_experience": "control",
            "reduced_tos_test_group": "control",
            "should_show_spi_before_conf": True,
            "google_oauth_account": None,
            "is_reg_request_from_ig_suma": False,
            "is_igios_spc_reg": False,
            "device_emails": [],
            "is_toa_reg": False,
            "is_threads_public": False,
            "spc_import_flow": False,
            "caa_play_integrity_attestation_result": None,
            "flash_call_provider": None,
            "name_prefill_variant": "control",
            "spc_birthday_input": False,
            "failed_birthday_year_count": None,
            "user_presented_medium_source": None
          }),
          "flow_info": json.dumps({
            "flow_name": "new_to_family_fb_default",
            "flow_type": "ntf"
          }),
          "current_step": 6,
          "INTERNAL_INFRA_screen_id": "hbtlb:6"
        }),
        "client_input_params": json.dumps({
          "lois_settings": json.dumps({
            "lois_token": "",
            "lara_override": ""
          })
        })
      })
    }
  
  def data_lanjutkan(self, mail):
    self.mail = mail
    return {
      "params": json.dumps({
        "server_params": json.dumps({
          "waterfall_id": "{}".format(self.uid1),
          "is_platform_login": 0,
          "is_from_logged_out": 0,
          "access_flow_version": "F2_FLOW",
          "tos_type": "standard",
          "reg_info": json.dumps({
            "first_name": "{}".format(self.firstnama),
            "last_name": "{}".format(self.lastnama),
            "full_name": "{}".format(self.firstnama),
            "contactpoint": "{}".format(self.mail),
            "ar_contactpoint": None,
            "contactpoint_type": "email",
            "is_using_unified_cp": False,
            "unified_cp_screen_variant": None,
            "is_cp_auto_confirmed": False,
            "is_cp_auto_confirmable": False,
            "confirmation_code": None,
            "birthday": "{}".format(self.tgl),
            "did_use_age": False,
            "gender": self.gender,
            "use_custom_gender": False,
            "custom_gender": None,
            "encrypted_password": "#PWD_BROWSER:0:{}:{}".format(self.timer,self.pw),
            "username": None,
            "username_prefill": None,
            "fb_conf_source": None,
            "device_id": None,
            "ig4a_qe_device_id": None,
            "family_device_id": None,
            "nta_eligibility_reason": None,
            "ig_nta_test_group": None,
            "user_id": None,
            "safetynet_token": None,
            "safetynet_response": None,
            "machine_id": None,
            "profile_photo": None,
            "profile_photo_id": None,
            "profile_photo_upload_id": None,
            "avatar": None,
            "email_oauth_token_no_contact_perm": None,
            "email_oauth_token": None,
            "email_oauth_tokens": [],
            "should_skip_two_step_conf": None,
            "openid_tokens_for_testing": None,
            "encrypted_msisdn": None,
            "encrypted_msisdn_for_safetynet": None,
            "cached_headers_safetynet_info": None,
            "should_skip_headers_safetynet": None,
            "headers_last_infra_flow_id": None,
            "headers_last_infra_flow_id_safetynet": None,
            "headers_flow_id": None,
            "was_headers_prefill_available": None,
            "sso_enabled": None,
            "existing_accounts": None,
            "used_ig_birthday": None,
            "sync_info": None,
            "create_new_to_app_account": None,
            "skip_session_info": None,
            "ck_error": None,
            "ck_id": None,
            "ck_nonce": None,
            "should_save_password": False,
            "horizon_synced_username": None,
            "fb_access_token": None,
            "horizon_synced_profile_pic": None,
            "is_identity_synced": False,
            "is_msplit_reg": None,
            "user_id_of_msplit_creator": None,
            "dma_data_combination_consent_given": None,
            "xapp_accounts": None,
            "fb_device_id": None,
            "fb_machine_id": None,
            "ig_device_id": None,
            "ig_machine_id": None,
            "should_skip_nta_upsell": None,
            "big_blue_token": None,
            "skip_sync_step_nta": None,
            "caa_reg_flow_source": None,
            "ig_authorization_token": None,
            "full_sheet_flow": False,
            "crypted_user_id": None,
            "is_caa_perf_enabled": False,
            "is_preform": True,
            "ignore_suma_check": False,
            "ignore_existing_login": False,
            "ignore_existing_login_from_suma": False,
            "ignore_existing_login_after_errors": False,
            "suggested_first_name": None,
            "suggested_last_name": None,
            "suggested_full_name": None,
            "replace_id_sync_variant": None,
            "is_redirect_from_nta_replace_id_sync_variant": False,
            "frl_authorization_token": None,
            "post_form_errors": None,
            "skip_step_without_errors": False,
            "existing_account_exact_match_checked": False,
            "existing_account_fuzzy_match_checked": False,
            "email_oauth_exists": False,
            "confirmation_code_send_error": None,
            "is_too_young": False,
            "source_account_type": None,
            "whatsapp_installed_on_client": False,
            "confirmation_medium": None,
            "source_credentials_type": None,
            "source_cuid": None,
            "source_account_reg_info": None,
            "soap_creation_source": None,
            "source_account_type_to_reg_info": None,
            "registration_flow_id": "",
            "should_skip_youth_tos": False,
            "is_youth_regulation_flow_complete": False,
            "is_on_cold_start": False,
            "email_prefilled": False,
            "cp_confirmed_by_auto_conf": False,
            "auto_conf_info": None,
            "in_sowa_experiment": False,
            "youth_regulation_config": None,
            "conf_allow_back_nav_after_change_cp": None,
            "conf_bouncing_cliff_screen_type": None,
            "conf_show_bouncing_cliff": None,
            "eligible_to_flash_call_in_ig4a": False,
            "flash_call_permissions_status": None,
            "attestation_result": None,
            "request_data_and_challenge_nonce_string": None,
            "confirmed_cp_and_code": None,
            "notification_callback_id": None,
            "reg_suma_state": 0,
            "is_msplit_neutral_choice": False,
            "msg_previous_cp": None,
            "ntp_import_source_info": None,
            "youth_consent_decision_time": None,
            "username_screen_experience": "control",
            "reduced_tos_test_group": "control",
            "should_show_spi_before_conf": True,
            "google_oauth_account": None,
            "is_reg_request_from_ig_suma": False,
            "is_igios_spc_reg": False,
            "device_emails": [],
            "is_toa_reg": False,
            "is_threads_public": False,
            "spc_import_flow": False,
            "caa_play_integrity_attestation_result": None,
            "flash_call_provider": None,
            "name_prefill_variant": "control",
            "spc_birthday_input": False,
            "failed_birthday_year_count": None,
            "user_presented_medium_source": None
          }),
          "flow_info": json.dumps({
            "flow_name": "new_to_family_fb_default",
            "flow_type": "ntf"
          }),
          "current_step": 8,
          "INTERNAL_INFRA_screen_id": "CAA_REG_TERMS_OF_SERVICE"
        }),
        "client_input_params": json.dumps({
          "lois_settings": json.dumps({
            "lois_token": "",
            "lara_override": ""
          })
        })
      })
    }
  
  def data_konfirmasi(self, mail):
    self.mail = mail
    return {
      "params": json.dumps({
          "server_params": json.dumps({
              "event_request_id": "{}".format(self.uid),
              "app_id": 0,
              "reg_info": json.dumps({
                  "first_name": "{}".format(self.firstnama),
                  "last_name": "{}".format(self.lastnama),
                  "full_name": "{}".format(self.firstnama),
                  "contactpoint": "{}".format(self.mail),
                  "ar_contactpoint": None,
                  "contactpoint_type": "email",
                  "is_using_unified_cp": False,
                  "unified_cp_screen_variant": None,
                  "is_cp_auto_confirmed": False,
                  "is_cp_auto_confirmable": False,
                  "confirmation_code": None,
                  "birthday": "{}".format(self.tgl),
                  "did_use_age": False,
                  "gender": self.gender,
                  "use_custom_gender": False,
                  "custom_gender": None,
                  "encrypted_password": "#PWD_BROWSER:0:{}:{}".format(self.timer,self.pw),
                  "username": None,
                  "username_prefill": None,
                  "fb_conf_source": None,
                  "device_id": None,
                  "ig4a_qe_device_id": None,
                  "family_device_id": None,
                  "nta_eligibility_reason": None,
                  "ig_nta_test_group": None,
                  "user_id": None,
                  "safetynet_token": None,
                  "safetynet_response": None,
                  "machine_id": None,
                  "profile_photo": None,
                  "profile_photo_id": None,
                  "profile_photo_upload_id": None,
                  "avatar": None,
                  "email_oauth_token_no_contact_perm": None,
                  "email_oauth_token": None,
                  "email_oauth_tokens": [],
                  "should_skip_two_step_conf": None,
                  "openid_tokens_for_testing": None,
                  "encrypted_msisdn": None,
                  "encrypted_msisdn_for_safetynet": None,
                  "cached_headers_safetynet_info": None,
                  "should_skip_headers_safetynet": None,
                  "headers_last_infra_flow_id": None,
                  "headers_last_infra_flow_id_safetynet": None,
                  "headers_flow_id": None,
                  "was_headers_prefill_available": None,
                  "sso_enabled": None,
                  "existing_accounts": None,
                  "used_ig_birthday": None,
                  "sync_info": None,
                  "create_new_to_app_account": None,
                  "skip_session_info": None,
                  "ck_error": None,
                  "ck_id": None,
                  "ck_nonce": None,
                  "should_save_password": False,
                  "horizon_synced_username": None,
                  "fb_access_token": None,
                  "horizon_synced_profile_pic": None,
                  "is_identity_synced": False,
                  "is_msplit_reg": None,
                  "user_id_of_msplit_creator": None,
                  "dma_data_combination_consent_given": None,
                  "xapp_accounts": None,
                  "fb_device_id": None,
                  "fb_machine_id": None,
                  "ig_device_id": None,
                  "ig_machine_id": None,
                  "should_skip_nta_upsell": None,
                  "big_blue_token": None,
                  "skip_sync_step_nta": None,
                  "caa_reg_flow_source": None,
                  "ig_authorization_token": None,
                  "full_sheet_flow": False,
                  "crypted_user_id": None,
                  "is_caa_perf_enabled": False,
                  "is_preform": True,
                  "ignore_suma_check": False,
                  "ignore_existing_login": False,
                  "ignore_existing_login_from_suma": False,
                  "ignore_existing_login_after_errors": False,
                  "suggested_first_name": None,
                  "suggested_last_name": None,
                  "suggested_full_name": None,
                  "replace_id_sync_variant": None,
                  "is_redirect_from_nta_replace_id_sync_variant": False,
                  "frl_authorization_token": None,
                  "post_form_errors": None,
                  "skip_step_without_errors": False,
                  "existing_account_exact_match_checked": False,
                  "existing_account_fuzzy_match_checked": False,
                  "email_oauth_exists": False,
                  "confirmation_code_send_error": None,
                  "is_too_young": False,
                  "source_account_type": None,
                  "whatsapp_installed_on_client": False,
                  "confirmation_medium": None,
                  "source_credentials_type": None,
                  "source_cuid": None,
                  "source_account_reg_info": None,
                  "soap_creation_source": None,
                  "source_account_type_to_reg_info": None,
                  "registration_flow_id": "",
                  "should_skip_youth_tos": False,
                  "is_youth_regulation_flow_complete": False,
                  "is_on_cold_start": False,
                  "email_prefilled": False,
                  "cp_confirmed_by_auto_conf": False,
                  "auto_conf_info": None,
                  "in_sowa_experiment": False,
                  "youth_regulation_config": None,
                  "conf_allow_back_nav_after_change_cp": None,
                  "conf_bouncing_cliff_screen_type": None,
                  "conf_show_bouncing_cliff": None,
                  "eligible_to_flash_call_in_ig4a": False,
                  "flash_call_permissions_status": None,
                  "attestation_result": None,
                  "request_data_and_challenge_nonce_string": None,
                  "confirmed_cp_and_code": None,
                  "notification_callback_id": None,
                  "reg_suma_state": 0,
                  "is_msplit_neutral_choice": False,
                  "msg_previous_cp": None,
                  "ntp_import_source_info": None,
                  "youth_consent_decision_time": None,
                  "username_screen_experience": "control",
                  "reduced_tos_test_group": "control",
                  "should_show_spi_before_conf": True,
                  "google_oauth_account": None,
                  "is_reg_request_from_ig_suma": False,
                  "is_igios_spc_reg": False,
                  "device_emails": [],
                  "is_toa_reg": False,
                  "is_threads_public": False,
                  "spc_import_flow": False,
                  "caa_play_integrity_attestation_result": None,
                  "flash_call_provider": None,
                  "name_prefill_variant": "control",
                  "spc_birthday_input": False,
                  "failed_birthday_year_count": None,
                  "user_presented_medium_source": None
              }),
              "flow_info": json.dumps({
                  "flow_name": "new_to_family_fb_default",
                  "flow_type": "ntf"
              }),
              "current_step": 8,
              "INTERNAL__latency_qpl_marker_id": 36707139,
              "INTERNAL__latency_qpl_instance_id": "2939614500017",
              "device_id": None,
              "family_device_id": None,
              "waterfall_id": "{}".format(self.uid1),
              "offline_experiment_group": None,
              "layered_homepage_experiment_group": None,
              "is_platform_login": 0,
              "is_from_logged_in_switcher": 0,
              "is_from_logged_out": 0,
              "access_flow_version": "F2_FLOW",
              "INTERNAL_INFRA_THEME": "harm_f"
          }),
          "client_input_params": json.dumps({
              "device_id": "",
              "waterfall_id": "{}".format(self.uid1),
              "machine_id": "",
              "ck_error": "",
              "ck_id": "",
              "ck_nonce": "",
              "should_ignore_existing_login": 0,
              "encrypted_msisdn": "",
              "headers_last_infra_flow_id": "",
              "reached_from_tos_screen": 1,
              "no_contact_perm_email_oauth_token": "",
              "failed_birthday_year_count": "{}",
              "lois_settings": json.dumps({
                  "lois_token": "",
                  "lara_override": ""
              })
          })
      })
    }
  
class Main:
  def __init__(self):
    self.xyz = requests.Session()
    self.pwww = Console().input('[grey50]Masukan Password:  [green]')
    self.mail = Requ().createMail()
  
  def timer(self, seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timeformat = '[white]Tunggu Detik: [green]{:02d}:{:02d}'.format(mins, secs)
        Console().print(timeformat, end='\r')
        time.sleep(1)
        seconds -= 1
        
  def Create_Nama(self):
    self.req = self.xyz.get("https://m.facebook.com/reg", headers=headersGet).text
    self.instance = Require()
    params = self.instance.data_nama()
    data = {
      "__aaid": "0",
      "__user": "0",
      "__a": "1",
      "__req": "m",
      "__hs": re.search('"haste_session":"(.*?)"',str(self.req)).group(1),
      "dpr": "1",
      "__ccg": re.search('"connectionClass":"(.*?)"',str(self.req)).group(1),
      "__rev": re.search('"__spin_r":(\d+)',str(self.req)).group(1),
      "__s": "",
      "__hsi": re.search('"hsi":"(\d+)"',str(self.req)).group(1),
      "__dyn": "",
      "__csr": "",
      "fb_dtsg": re.search('"dtsg":{"token":"(.*?)"',str(self.req)).group(1),
      "jazoest": "24932",
      "lsd": re.search('"lsd":"(.*?)"',str(self.req)).group(1),
      "params": json.dumps(params)
    }
    res1 = self.xyz.post("https://m.facebook.com/async/wbloks/fetch/?appid=com.bloks.www.bloks.caa.reg.name.async&type=action&__bkv=4ee95c9e553a9a2c2baf8318b0a826bd7867d57d580f6d0cea277fc114bece98", data=data, headers=headersPost).text

  def Response_Nama(self):
    params = self.instance.response_nama()
    data = {
      "__aaid": 0,
      "__user": 0,
      "__a": 1,
      "__req": "n",
      "__hs": re.search('"haste_session":"(.*?)"',str(self.req)).group(1),
      "dpr": 1,
      "__ccg": re.search('"connectionClass":"(.*?)"',str(self.req)).group(1),
      "__rev": re.search('"__spin_r":(\d+)',str(self.req)).group(1),
      "__s": "",
      "__hsi": re.search('"hsi":"(\d+)"',str(self.req)).group(1),
      "__dyn": "",
      "__csr": "",
      "fb_dtsg": re.search('"dtsg":{"token":"(.*?)"',str(self.req)).group(1),
      "jazoest": "24932",
      "lsd": re.search('"lsd":"(.*?)"',str(self.req)).group(1),
      "params": json.dumps(params)
    }
    res2 = self.xyz.post("https://m.facebook.com/async/wbloks/fetch/?appid=com.bloks.www.bloks.caa.reg.birthday&type=app&__bkv=4ee95c9e553a9a2c2baf8318b0a826bd7867d57d580f6d0cea277fc114bece98", data=data, headers=headersPost).text
    
  
  def Create_Birthday(self):
    params = self.instance.data_birthday()
    data = {
      "__aaid": 0,
      "__user": 0,
      "__a": 1,
      "__req": "p",
      "__hs": re.search('"haste_session":"(.*?)"',str(self.req)).group(1),
      "dpr": 1,
      "__ccg": re.search('"connectionClass":"(.*?)"',str(self.req)).group(1),
      "__rev": re.search('"__spin_r":(\d+)',str(self.req)).group(1),
      "__s": "",
      "__hsi": re.search('"hsi":"(\d+)"',str(self.req)).group(1),
      "__dyn": "",
      "__csr": "",
      "fb_dtsg": re.search('"dtsg":{"token":"(.*?)"',str(self.req)).group(1),
      "jazoest": "24932",
      "lsd": re.search('"lsd":"(.*?)"',str(self.req)).group(1),
      "params": json.dumps(params)
    }
    
    res3 = self.xyz.post("https://m.facebook.com/async/wbloks/fetch/?appid=com.bloks.www.bloks.caa.reg.birthday.async&type=action&__bkv=4ee95c9e553a9a2c2baf8318b0a826bd7867d57d580f6d0cea277fc114bece98", data=data, headers=headersPost).text    
    
  def Response_Birthday(self):
    params = self.instance.response_birthday()
    data = {
      "__aaid": 0,
      "__user": 0,
      "__a": 1,
      "__req": "q",
      "__hs": re.search('"haste_session":"(.*?)"',str(self.req)).group(1),
      "dpr": 1,
      "__ccg": re.search('"connectionClass":"(.*?)"',str(self.req)).group(1),
      "__rev": re.search('"__spin_r":(\d+)',str(self.req)).group(1),
      "__s": "",
      "__hsi": re.search('"hsi":"(\d+)"',str(self.req)).group(1),
      "__dyn": "",
      "__csr": "",
      "fb_dtsg": re.search('"dtsg":{"token":"(.*?)"',str(self.req)).group(1),
      "jazoest": "24932",
      "lsd": re.search('"lsd":"(.*?)"',str(self.req)).group(1),
      "params": json.dumps(params)
    }
    res4 = self.xyz.post("https://m.facebook.com/async/wbloks/fetch/?appid=com.bloks.www.bloks.caa.reg.gender&type=app&__bkv=4ee95c9e553a9a2c2baf8318b0a826bd7867d57d580f6d0cea277fc114bece98",data=data, headers=headersPost).text    
    
  def Create_Gender(self):
    params = self.instance.data_gender()
    data = {
      "__aaid": 0,
      "__user": 0,
      "__a": 1,
      "__req": "t",
      "__hs": re.search('"haste_session":"(.*?)"',str(self.req)).group(1),
      "dpr": 1,
      "__ccg": re.search('"connectionClass":"(.*?)"',str(self.req)).group(1),
      "__rev": re.search('"__spin_r":(\d+)',str(self.req)).group(1),
      "__s": "",
      "__hsi": re.search('"hsi":"(\d+)"',str(self.req)).group(1),
      "__dyn": "",
      "__csr": "",
      "fb_dtsg": re.search('"dtsg":{"token":"(.*?)"',str(self.req)).group(1),
      "jazoest": "24932",
      "lsd": re.search('"lsd":"(.*?)"',str(self.req)).group(1),
      "params": json.dumps(params)
    }
    res5 = self.xyz.post("https://m.facebook.com/async/wbloks/fetch/?appid=com.bloks.www.bloks.caa.reg.gender.async&type=action&__bkv=4ee95c9e553a9a2c2baf8318b0a826bd7867d57d580f6d0cea277fc114bece98", data=data, headers=headersPost).text     
    
  def Response_Gender(self):
    params = self.instance.response_gender()
    data = {
      "__aaid": 0,
      "__user": 0,
      "__a": 1,
      "__req": "u",
      "__hs": re.search('"haste_session":"(.*?)"',str(self.req)).group(1),
      "dpr": 1,
      "__ccg": re.search('"connectionClass":"(.*?)"',str(self.req)).group(1),
      "__rev": re.search('"__spin_r":(\d+)',str(self.req)).group(1),
      "__s": "",
      "__hsi": re.search('"hsi":"(\d+)"',str(self.req)).group(1),
      "__dyn": "",
      "__csr": "",
      "fb_dtsg": re.search('"dtsg":{"token":"(.*?)"',str(self.req)).group(1),
      "jazoest": "24932",
      "lsd": re.search('"lsd":"(.*?)"',str(self.req)).group(1),
      "params": json.dumps(params)
    }
    res6 = self.xyz.post("https://m.facebook.com/async/wbloks/fetch/?appid=com.bloks.www.bloks.caa.reg.contactpoint_email&type=app&__bkv=4ee95c9e553a9a2c2baf8318b0a826bd7867d57d580f6d0cea277fc114bece98", data=data, headers=headersPost).text 
  
  def Create_Email(self):
    params = self.instance.data_email(self.mail)
    data = {
      "__aaid": 0,
      "__user": 0,
      "__a": 1,
      "__req": "12",
      "__hs": re.search('"haste_session":"(.*?)"',str(self.req)).group(1),
      "dpr": 1,
      "__ccg": re.search('"connectionClass":"(.*?)"',str(self.req)).group(1),
      "__rev": re.search('"__spin_r":(\d+)',str(self.req)).group(1),
      "__s": "",
      "__hsi": re.search('"hsi":"(\d+)"',str(self.req)).group(1),
      "__dyn": "",
      "__csr": "",
      "fb_dtsg": re.search('"dtsg":{"token":"(.*?)"',str(self.req)).group(1),
      "jazoest": "24932",
      "lsd": re.search('"lsd":"(.*?)"',str(self.req)).group(1),
      "params": json.dumps(params)
    }
    res7 = self.xyz.post("https://m.facebook.com/async/wbloks/fetch/?appid=com.bloks.www.bloks.caa.reg.async.contactpoint_email.async&type=action&__bkv=4ee95c9e553a9a2c2baf8318b0a826bd7867d57d580f6d0cea277fc114bece98", data=data, headers=headersPost).text    
   
  def Response_Email(self):
    params = self.instance.response_email(self.mail)
    data = {
      "__aaid": 0,
      "__user": 0,
      "__a": 1,
      "__req": "14",
      "__hs": re.search('"haste_session":"(.*?)"',str(self.req)).group(1),
      "dpr": 1,
      "__ccg": re.search('"connectionClass":"(.*?)"',str(self.req)).group(1),
      "__rev": re.search('"__spin_r":(\d+)',str(self.req)).group(1),
      "__s": "",
      "__hsi": re.search('"hsi":"(\d+)"',str(self.req)).group(1),
      "__dyn": "",
      "__csr": "",
      "fb_dtsg": re.search('"dtsg":{"token":"(.*?)"',str(self.req)).group(1),
      "jazoest": "24932",
      "lsd": re.search('"lsd":"(.*?)"',str(self.req)).group(1),
      "params": json.dumps(params)
    }
    res8 = self.xyz.post("https://m.facebook.com/async/wbloks/fetch/?appid=com.bloks.www.bloks.caa.reg.password&type=app&__bkv=4ee95c9e553a9a2c2baf8318b0a826bd7867d57d580f6d0cea277fc114bece98", data=data, headers=headersPost).text   
  
  def Create_Password(self):
    params = self.instance.data_password(self.mail)
    data = {
      "__aaid": 0,
      "__user": 0,
      "__a": 1,
      "__req": "17",
      "__hs": re.search('"haste_session":"(.*?)"',str(self.req)).group(1),
      "dpr": 1,
      "__ccg": re.search('"connectionClass":"(.*?)"',str(self.req)).group(1),
      "__rev": re.search('"__spin_r":(\d+)',str(self.req)).group(1),
      "__s": "",
      "__hsi": re.search('"hsi":"(\d+)"',str(self.req)).group(1),
      "__dyn": "",
      "__csr": "",
      "fb_dtsg": re.search('"dtsg":{"token":"(.*?)"',str(self.req)).group(1),
      "jazoest": "24932",
      "lsd": re.search('"lsd":"(.*?)"',str(self.req)).group(1),
      "params": json.dumps(params)
    }
    res9 = self.xyz.post("https://m.facebook.com/async/wbloks/fetch/?appid=com.bloks.www.bloks.caa.reg.password.async&type=action&__bkv=4ee95c9e553a9a2c2baf8318b0a826bd7867d57d580f6d0cea277fc114bece98", data=data, headers=headersPost).text    
   
  def Response_Password(self):
    params = self.instance.response_password(self.mail)
    data = {
      "__aaid": 0,
      "__user": 0,
      "__a": 1,
      "__req": "18",
      "__hs": re.search('"haste_session":"(.*?)"',str(self.req)).group(1),
      "dpr": 1,
      "__ccg": re.search('"connectionClass":"(.*?)"',str(self.req)).group(1),
      "__rev": re.search('"__spin_r":(\d+)',str(self.req)).group(1),
      "__s": "",
      "__hsi": re.search('"hsi":"(\d+)"',str(self.req)).group(1),
      "__dyn": "",
      "__csr": "",
      "fb_dtsg": re.search('"dtsg":{"token":"(.*?)"',str(self.req)).group(1),
      "jazoest": "24932",
      "lsd": re.search('"lsd":"(.*?)"',str(self.req)).group(1),
      "params": json.dumps(params)
    }
    res9 = self.xyz.post("https://m.facebook.com/async/wbloks/fetch/?appid=com.bloks.www.bloks.caa.reg.save-credentials&type=app&__bkv=4ee95c9e553a9a2c2baf8318b0a826bd7867d57d580f6d0cea277fc114bece98", data=data, headers=headersPost).text    
    
  def Next_Response(self):
    params = self.instance.data_lanjutkan(self.mail)
    data = {
      "__aaid": 0,
      "__user": 0,
      "__a": 1,
      "__req": "1a",
      "__hs": re.search('"haste_session":"(.*?)"',str(self.req)).group(1),
      "dpr": 1,
      "__ccg": re.search('"connectionClass":"(.*?)"',str(self.req)).group(1),
      "__rev": re.search('"__spin_r":(\d+)',str(self.req)).group(1),
      "__s": "",
      "__hsi": re.search('"hsi":"(\d+)"',str(self.req)).group(1),
      "__dyn": "",
      "__csr": "",
      "fb_dtsg": re.search('"dtsg":{"token":"(.*?)"',str(self.req)).group(1),
      "jazoest": "24932",
      "lsd": re.search('"lsd":"(.*?)"',str(self.req)).group(1),
      "params": json.dumps(params)
    }
    res10 = self.xyz.post("https://m.facebook.com/async/wbloks/fetch/?appid=com.bloks.www.bloks.caa.reg.tos&type=app&__bkv=4ee95c9e553a9a2c2baf8318b0a826bd7867d57d580f6d0cea277fc114bece98", data=data, headers=headersPost).text       
   
  def Next_Konfirmasi(self):
    params = self.instance.data_konfirmasi(self.mail)
    data = {
      "__aaid": 0,
      "__user": 0,
      "__a": 1,
      "__req": "1c",
      "__hs": re.search('"haste_session":"(.*?)"',str(self.req)).group(1),
      "dpr": 1,
      "__ccg": re.search('"connectionClass":"(.*?)"',str(self.req)).group(1),
      "__rev": re.search('"__spin_r":(\d+)',str(self.req)).group(1),
      "__s": "",
      "__hsi": re.search('"hsi":"(\d+)"',str(self.req)).group(1),
      "__dyn": "",
      "__csr": "",
      "fb_dtsg": re.search('"dtsg":{"token":"(.*?)"',str(self.req)).group(1),
      "jazoest": "24932",
      "lsd": re.search('"lsd":"(.*?)"',str(self.req)).group(1),
      "params": json.dumps(params)
    }
    res11 = self.xyz.post("https://m.facebook.com/async/wbloks/fetch/?appid=com.bloks.www.bloks.caa.reg.create.account.async&type=action&__bkv=4ee95c9e553a9a2c2baf8318b0a826bd7867d57d580f6d0cea277fc114bece98", data=data, headers=headersPost).text 
    if "session_key" in str(res11):
      self.uids = re.search('"uid":(\d+)', res11.replace('\\','')).group(1)
      self.Next_Konfirmasi2(self.uids)
    else: 
      Console().print("[grey50] ID akun facebook: [red]tidak di temukan")    
  
  def Next_Konfirmasi2(self, uid):
    self.timer(5); print()
    kode = RequKd().Kodekonfirmasi(self.mail)
    header = {
      'authority': 'm.facebook.com',
      'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
      'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
      'cache-control': 'max-age=0',
      'dpr': '2',
      'referer': 'https://m.facebook.com/login/save-device/',
      'sec-ch-prefers-color-scheme': 'light',
      'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="125", "Google Chrome";v="125"',
      'sec-ch-ua-mobile': '?1',
      'sec-ch-ua-platform': '"Android"',
      'sec-fetch-dest': 'document',
      'sec-fetch-mode': 'navigate',
      'sec-fetch-site': 'same-origin',
      'sec-fetch-user': '?1',
      'upgrade-insecure-requests': '1',
      'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Mobile Safari/537.36',
      'viewport-width': '980',      
    }
    params = {
      'next': 'https://m.facebook.com/?deoia=1',
      'soft': 'hjk',
    }
    respon = self.xyz.get('https://m.facebook.com/confirmemail.php', params=params, headers=header).text    
    headers = {
      'authority': 'm.facebook.com',
      'accept': '*/*',
      'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
      'content-type': 'application/x-www-form-urlencoded',
      'origin': 'https://m.facebook.com',
      'referer': 'https://m.facebook.com/confirmemail.php',
      'sec-ch-prefers-color-scheme': 'light',
      'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="125", "Google Chrome";v="125"',
      'sec-ch-ua-mobile': '?1',
      'sec-ch-ua-platform': '"Android"',
      'sec-fetch-dest': 'empty',
      'sec-fetch-mode': 'cors',
      'sec-fetch-site': 'same-origin',
      'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Mobile Safari/537.36',
      'x-asbd-id': '129477',
      'x-fb-lsd': 'ItVSr8mi45_8vvNpKLDMB5',
    }
    params1 = {
      'contact': '{}'.format(self.mail),
      'type': 'submit',
      'is_soft_cliff': 'false',
      'medium': 'email',
      'code': '{}'.format(kode),
    }
    data = {
      'fb_dtsg': re.search('"dtsg":{"token":"(.*?)"',str(respon)).group(1),
      'jazoest': re.search(r'"\d+"', respon).group().strip('"'),#'25381',
      'lsd': re.search('"LSD",\[\],{"token":"([^"]+)"}',str(respon)).group(1),
      '__dyn': '',
      '__csr': '',
      '__req': '4',
      '__fmt': '1',
      '__a': '',
      '__user': f'{uid}',
    }    
    response = self.xyz.post('https://m.facebook.com/confirmation_cliff/', params=params1, headers=headers, data=data)    
    if "home.php?confirmed_account" in str(response.text):
      cookies = '; '.join([f'{key}={value}' for key, value in self.xyz.cookies.get_dict().items()])  
      RequLink().Bahasa(cookies); RequLink().FLCookies(cookies); RequLink().ReactPost(cookies)  
      payloads = self.instance.ResponseAkun()
      self.firstnama, self.lastnama, self.pw, self.tgl = self.instance.ResponseSM()
      print("""{}{{
   {}status{}: {}success
   {}informations{}: {{{}
        {}email{}: {}{}
        {}kode{}: {}{}
        {}user{}: {}{}{}
        {}url{}: {}https://www.facebook.com/{}{}
        {}cookies{}: {}{}
    }}
}}""".format(p, m, p, h, m, p, payloads, m, p, h, self.mail, m, p, h, kode, m, p, h, uid, p, m, p, h, uid, p, m, p, h, cookies))
      with open("success.txt","a") as wr:
        wr.write(f"{uid}|{self.firstnama} {self.lastnama}|{self.pw}|{self.mail}\n")
        wr.close()

      filename = f"successID{self.pw}.txt"
      
      with open(filename, "a") as wr:
        wr.write(f"{uid}\n")
        wr.close()
    else:
      payloads = self.instance.ResponseAkun2()
      self.firstnama, self.lastnama, self.pw, self.tgl = self.instance.ResponseSM()
      print("""{}{{
   {}status{}: {}invalid
   {}informations{}: {{{}
        {}email{}: {}{}
        {}kode{}: {}{}
        {}user{}: {}{}{}
        {}url{}: {}https://www.facebook.com/{}{}
    }}
}}""".format(p, m, p, k, m, p, payloads, m, p, k, self.mail, m, p, k, kode, m, p, k, uid, p, m, p, k, uid, p))
      with open("create_facebook_invalid.txt","a") as wr:
        wr.write(f"{uid}|{self.firstnama} {self.lastnama}|{self.pw}|{self.tgl}|{self.mail}|{kode}\n")
        wr.close()
        
class MainV2:
  def __init__(self):
    self.xyz = requests.Session()
    self.mail = Console().input('[grey50]Masukan alamat email:  [green]')
  
  def timer(self, seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timeformat = '[white]Tunggu Detik: [green]{:02d}:{:02d}'.format(mins, secs)
        Console().print(timeformat, end='\r')
        time.sleep(1)
        seconds -= 1
        
  def Create_Nama(self):
    self.req = self.xyz.get("https://m.facebook.com/reg", headers=headersGet).text
    self.instance = Require()
    params = self.instance.data_nama()
    data = {
      "__aaid": "0",
      "__user": "0",
      "__a": "1",
      "__req": "m",
      "__hs": re.search('"haste_session":"(.*?)"',str(self.req)).group(1),
      "dpr": "1",
      "__ccg": re.search('"connectionClass":"(.*?)"',str(self.req)).group(1),
      "__rev": re.search('"__spin_r":(\d+)',str(self.req)).group(1),
      "__s": "",
      "__hsi": re.search('"hsi":"(\d+)"',str(self.req)).group(1),
      "__dyn": "",
      "__csr": "",
      "fb_dtsg": re.search('"dtsg":{"token":"(.*?)"',str(self.req)).group(1),
      "jazoest": "24932",
      "lsd": re.search('"lsd":"(.*?)"',str(self.req)).group(1),
      "params": json.dumps(params)
    }
    res1 = self.xyz.post("https://m.facebook.com/async/wbloks/fetch/?appid=com.bloks.www.bloks.caa.reg.name.async&type=action&__bkv=4ee95c9e553a9a2c2baf8318b0a826bd7867d57d580f6d0cea277fc114bece98", data=data, headers=headersPost).text

  def Response_Nama(self):
    params = self.instance.response_nama()
    data = {
      "__aaid": 0,
      "__user": 0,
      "__a": 1,
      "__req": "n",
      "__hs": re.search('"haste_session":"(.*?)"',str(self.req)).group(1),
      "dpr": 1,
      "__ccg": re.search('"connectionClass":"(.*?)"',str(self.req)).group(1),
      "__rev": re.search('"__spin_r":(\d+)',str(self.req)).group(1),
      "__s": "",
      "__hsi": re.search('"hsi":"(\d+)"',str(self.req)).group(1),
      "__dyn": "",
      "__csr": "",
      "fb_dtsg": re.search('"dtsg":{"token":"(.*?)"',str(self.req)).group(1),
      "jazoest": "24932",
      "lsd": re.search('"lsd":"(.*?)"',str(self.req)).group(1),
      "params": json.dumps(params)
    }
    res2 = self.xyz.post("https://m.facebook.com/async/wbloks/fetch/?appid=com.bloks.www.bloks.caa.reg.birthday&type=app&__bkv=4ee95c9e553a9a2c2baf8318b0a826bd7867d57d580f6d0cea277fc114bece98", data=data, headers=headersPost).text
    
  
  def Create_Birthday(self):
    params = self.instance.data_birthday()
    data = {
      "__aaid": 0,
      "__user": 0,
      "__a": 1,
      "__req": "p",
      "__hs": re.search('"haste_session":"(.*?)"',str(self.req)).group(1),
      "dpr": 1,
      "__ccg": re.search('"connectionClass":"(.*?)"',str(self.req)).group(1),
      "__rev": re.search('"__spin_r":(\d+)',str(self.req)).group(1),
      "__s": "",
      "__hsi": re.search('"hsi":"(\d+)"',str(self.req)).group(1),
      "__dyn": "",
      "__csr": "",
      "fb_dtsg": re.search('"dtsg":{"token":"(.*?)"',str(self.req)).group(1),
      "jazoest": "24932",
      "lsd": re.search('"lsd":"(.*?)"',str(self.req)).group(1),
      "params": json.dumps(params)
    }
    
    res3 = self.xyz.post("https://m.facebook.com/async/wbloks/fetch/?appid=com.bloks.www.bloks.caa.reg.birthday.async&type=action&__bkv=4ee95c9e553a9a2c2baf8318b0a826bd7867d57d580f6d0cea277fc114bece98", data=data, headers=headersPost).text    
    
  def Response_Birthday(self):
    params = self.instance.response_birthday()
    data = {
      "__aaid": 0,
      "__user": 0,
      "__a": 1,
      "__req": "q",
      "__hs": re.search('"haste_session":"(.*?)"',str(self.req)).group(1),
      "dpr": 1,
      "__ccg": re.search('"connectionClass":"(.*?)"',str(self.req)).group(1),
      "__rev": re.search('"__spin_r":(\d+)',str(self.req)).group(1),
      "__s": "",
      "__hsi": re.search('"hsi":"(\d+)"',str(self.req)).group(1),
      "__dyn": "",
      "__csr": "",
      "fb_dtsg": re.search('"dtsg":{"token":"(.*?)"',str(self.req)).group(1),
      "jazoest": "24932",
      "lsd": re.search('"lsd":"(.*?)"',str(self.req)).group(1),
      "params": json.dumps(params)
    }
    res4 = self.xyz.post("https://m.facebook.com/async/wbloks/fetch/?appid=com.bloks.www.bloks.caa.reg.gender&type=app&__bkv=4ee95c9e553a9a2c2baf8318b0a826bd7867d57d580f6d0cea277fc114bece98",data=data, headers=headersPost).text    
    
  def Create_Gender(self):
    params = self.instance.data_gender()
    data = {
      "__aaid": 0,
      "__user": 0,
      "__a": 1,
      "__req": "t",
      "__hs": re.search('"haste_session":"(.*?)"',str(self.req)).group(1),
      "dpr": 1,
      "__ccg": re.search('"connectionClass":"(.*?)"',str(self.req)).group(1),
      "__rev": re.search('"__spin_r":(\d+)',str(self.req)).group(1),
      "__s": "",
      "__hsi": re.search('"hsi":"(\d+)"',str(self.req)).group(1),
      "__dyn": "",
      "__csr": "",
      "fb_dtsg": re.search('"dtsg":{"token":"(.*?)"',str(self.req)).group(1),
      "jazoest": "24932",
      "lsd": re.search('"lsd":"(.*?)"',str(self.req)).group(1),
      "params": json.dumps(params)
    }
    res5 = self.xyz.post("https://m.facebook.com/async/wbloks/fetch/?appid=com.bloks.www.bloks.caa.reg.gender.async&type=action&__bkv=4ee95c9e553a9a2c2baf8318b0a826bd7867d57d580f6d0cea277fc114bece98", data=data, headers=headersPost).text     
    
  def Response_Gender(self):
    params = self.instance.response_gender()
    data = {
      "__aaid": 0,
      "__user": 0,
      "__a": 1,
      "__req": "u",
      "__hs": re.search('"haste_session":"(.*?)"',str(self.req)).group(1),
      "dpr": 1,
      "__ccg": re.search('"connectionClass":"(.*?)"',str(self.req)).group(1),
      "__rev": re.search('"__spin_r":(\d+)',str(self.req)).group(1),
      "__s": "",
      "__hsi": re.search('"hsi":"(\d+)"',str(self.req)).group(1),
      "__dyn": "",
      "__csr": "",
      "fb_dtsg": re.search('"dtsg":{"token":"(.*?)"',str(self.req)).group(1),
      "jazoest": "24932",
      "lsd": re.search('"lsd":"(.*?)"',str(self.req)).group(1),
      "params": json.dumps(params)
    }
    res6 = self.xyz.post("https://m.facebook.com/async/wbloks/fetch/?appid=com.bloks.www.bloks.caa.reg.contactpoint_email&type=app&__bkv=4ee95c9e553a9a2c2baf8318b0a826bd7867d57d580f6d0cea277fc114bece98", data=data, headers=headersPost).text 
  
  def Create_Email(self):
    params = self.instance.data_email(self.mail)
    data = {
      "__aaid": 0,
      "__user": 0,
      "__a": 1,
      "__req": "12",
      "__hs": re.search('"haste_session":"(.*?)"',str(self.req)).group(1),
      "dpr": 1,
      "__ccg": re.search('"connectionClass":"(.*?)"',str(self.req)).group(1),
      "__rev": re.search('"__spin_r":(\d+)',str(self.req)).group(1),
      "__s": "",
      "__hsi": re.search('"hsi":"(\d+)"',str(self.req)).group(1),
      "__dyn": "",
      "__csr": "",
      "fb_dtsg": re.search('"dtsg":{"token":"(.*?)"',str(self.req)).group(1),
      "jazoest": "24932",
      "lsd": re.search('"lsd":"(.*?)"',str(self.req)).group(1),
      "params": json.dumps(params)
    }
    res7 = self.xyz.post("https://m.facebook.com/async/wbloks/fetch/?appid=com.bloks.www.bloks.caa.reg.async.contactpoint_email.async&type=action&__bkv=4ee95c9e553a9a2c2baf8318b0a826bd7867d57d580f6d0cea277fc114bece98", data=data, headers=headersPost).text    
   
  def Response_Email(self):
    params = self.instance.response_email(self.mail)
    data = {
      "__aaid": 0,
      "__user": 0,
      "__a": 1,
      "__req": "14",
      "__hs": re.search('"haste_session":"(.*?)"',str(self.req)).group(1),
      "dpr": 1,
      "__ccg": re.search('"connectionClass":"(.*?)"',str(self.req)).group(1),
      "__rev": re.search('"__spin_r":(\d+)',str(self.req)).group(1),
      "__s": "",
      "__hsi": re.search('"hsi":"(\d+)"',str(self.req)).group(1),
      "__dyn": "",
      "__csr": "",
      "fb_dtsg": re.search('"dtsg":{"token":"(.*?)"',str(self.req)).group(1),
      "jazoest": "24932",
      "lsd": re.search('"lsd":"(.*?)"',str(self.req)).group(1),
      "params": json.dumps(params)
    }
    res8 = self.xyz.post("https://m.facebook.com/async/wbloks/fetch/?appid=com.bloks.www.bloks.caa.reg.password&type=app&__bkv=4ee95c9e553a9a2c2baf8318b0a826bd7867d57d580f6d0cea277fc114bece98", data=data, headers=headersPost).text   
  
  def Create_Password(self):
    params = self.instance.data_password(self.mail)
    data = {
      "__aaid": 0,
      "__user": 0,
      "__a": 1,
      "__req": "17",
      "__hs": re.search('"haste_session":"(.*?)"',str(self.req)).group(1),
      "dpr": 1,
      "__ccg": re.search('"connectionClass":"(.*?)"',str(self.req)).group(1),
      "__rev": re.search('"__spin_r":(\d+)',str(self.req)).group(1),
      "__s": "",
      "__hsi": re.search('"hsi":"(\d+)"',str(self.req)).group(1),
      "__dyn": "",
      "__csr": "",
      "fb_dtsg": re.search('"dtsg":{"token":"(.*?)"',str(self.req)).group(1),
      "jazoest": "24932",
      "lsd": re.search('"lsd":"(.*?)"',str(self.req)).group(1),
      "params": json.dumps(params)
    }
    res9 = self.xyz.post("https://m.facebook.com/async/wbloks/fetch/?appid=com.bloks.www.bloks.caa.reg.password.async&type=action&__bkv=4ee95c9e553a9a2c2baf8318b0a826bd7867d57d580f6d0cea277fc114bece98", data=data, headers=headersPost).text    
   
  def Response_Password(self):
    params = self.instance.response_password(self.mail)
    data = {
      "__aaid": 0,
      "__user": 0,
      "__a": 1,
      "__req": "18",
      "__hs": re.search('"haste_session":"(.*?)"',str(self.req)).group(1),
      "dpr": 1,
      "__ccg": re.search('"connectionClass":"(.*?)"',str(self.req)).group(1),
      "__rev": re.search('"__spin_r":(\d+)',str(self.req)).group(1),
      "__s": "",
      "__hsi": re.search('"hsi":"(\d+)"',str(self.req)).group(1),
      "__dyn": "",
      "__csr": "",
      "fb_dtsg": re.search('"dtsg":{"token":"(.*?)"',str(self.req)).group(1),
      "jazoest": "24932",
      "lsd": re.search('"lsd":"(.*?)"',str(self.req)).group(1),
      "params": json.dumps(params)
    }
    res9 = self.xyz.post("https://m.facebook.com/async/wbloks/fetch/?appid=com.bloks.www.bloks.caa.reg.save-credentials&type=app&__bkv=4ee95c9e553a9a2c2baf8318b0a826bd7867d57d580f6d0cea277fc114bece98", data=data, headers=headersPost).text    
    
  def Next_Response(self):
    params = self.instance.data_lanjutkan(self.mail)
    data = {
      "__aaid": 0,
      "__user": 0,
      "__a": 1,
      "__req": "1a",
      "__hs": re.search('"haste_session":"(.*?)"',str(self.req)).group(1),
      "dpr": 1,
      "__ccg": re.search('"connectionClass":"(.*?)"',str(self.req)).group(1),
      "__rev": re.search('"__spin_r":(\d+)',str(self.req)).group(1),
      "__s": "",
      "__hsi": re.search('"hsi":"(\d+)"',str(self.req)).group(1),
      "__dyn": "",
      "__csr": "",
      "fb_dtsg": re.search('"dtsg":{"token":"(.*?)"',str(self.req)).group(1),
      "jazoest": "24932",
      "lsd": re.search('"lsd":"(.*?)"',str(self.req)).group(1),
      "params": json.dumps(params)
    }
    res10 = self.xyz.post("https://m.facebook.com/async/wbloks/fetch/?appid=com.bloks.www.bloks.caa.reg.tos&type=app&__bkv=4ee95c9e553a9a2c2baf8318b0a826bd7867d57d580f6d0cea277fc114bece98", data=data, headers=headersPost).text       
   
  def Next_Konfirmasi(self):
    params = self.instance.data_konfirmasi(self.mail)
    data = {
      "__aaid": 0,
      "__user": 0,
      "__a": 1,
      "__req": "1c",
      "__hs": re.search('"haste_session":"(.*?)"',str(self.req)).group(1),
      "dpr": 1,
      "__ccg": re.search('"connectionClass":"(.*?)"',str(self.req)).group(1),
      "__rev": re.search('"__spin_r":(\d+)',str(self.req)).group(1),
      "__s": "",
      "__hsi": re.search('"hsi":"(\d+)"',str(self.req)).group(1),
      "__dyn": "",
      "__csr": "",
      "fb_dtsg": re.search('"dtsg":{"token":"(.*?)"',str(self.req)).group(1),
      "jazoest": "24932",
      "lsd": re.search('"lsd":"(.*?)"',str(self.req)).group(1),
      "params": json.dumps(params)
    }
    res11 = self.xyz.post("https://m.facebook.com/async/wbloks/fetch/?appid=com.bloks.www.bloks.caa.reg.create.account.async&type=action&__bkv=4ee95c9e553a9a2c2baf8318b0a826bd7867d57d580f6d0cea277fc114bece98", data=data, headers=headersPost).text 
    if "session_key" in str(res11):
      self.uids = re.search('"uid":(\d+)', res11.replace('\\','')).group(1)
      self.Next_Konfirmasi2(self.uids)
    else: 
      Console().print("[grey50]ID akun facebook: [red]tidak di temukan")    
  
  def Next_Konfirmasi2(self, uid):
    kode = Console().input('[grey50]Kode verifikasi: [green]')
    print()
    header = {
      'authority': 'm.facebook.com',
      'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
      'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
      'cache-control': 'max-age=0',
      'dpr': '2',
      'referer': 'https://m.facebook.com/login/save-device/',
      'sec-ch-prefers-color-scheme': 'light',
      'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="125", "Google Chrome";v="125"',
      'sec-ch-ua-mobile': '?1',
      'sec-ch-ua-platform': '"Android"',
      'sec-fetch-dest': 'document',
      'sec-fetch-mode': 'navigate',
      'sec-fetch-site': 'same-origin',
      'sec-fetch-user': '?1',
      'upgrade-insecure-requests': '1',
      'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Mobile Safari/537.36',
      'viewport-width': '980',      
    }
    params = {
      'next': 'https://m.facebook.com/?deoia=1',
      'soft': 'hjk',
    }
    respon = self.xyz.get('https://m.facebook.com/confirmemail.php', params=params, headers=header).text    
    headers = {
      'authority': 'm.facebook.com',
      'accept': '*/*',
      'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
      'content-type': 'application/x-www-form-urlencoded',
      'origin': 'https://m.facebook.com',
      'referer': 'https://m.facebook.com/confirmemail.php',
      'sec-ch-prefers-color-scheme': 'light',
      'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="125", "Google Chrome";v="125"',
      'sec-ch-ua-mobile': '?1',
      'sec-ch-ua-platform': '"Android"',
      'sec-fetch-dest': 'empty',
      'sec-fetch-mode': 'cors',
      'sec-fetch-site': 'same-origin',
      'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Mobile Safari/537.36',
      'x-asbd-id': '129477',
      'x-fb-lsd': 'ItVSr8mi45_8vvNpKLDMB5',
    }
    params1 = {
      'contact': '{}'.format(self.mail),
      'type': 'submit',
      'is_soft_cliff': 'false',
      'medium': 'email',
      'code': '{}'.format(kode),
    }
    data = {
      'fb_dtsg': re.search('"dtsg":{"token":"(.*?)"',str(respon)).group(1),
      'jazoest': re.search(r'"\d+"', respon).group().strip('"'),#'25381',
      'lsd': re.search('"LSD",\[\],{"token":"([^"]+)"}',str(respon)).group(1),
      '__dyn': '',
      '__csr': '',
      '__req': '4',
      '__fmt': '1',
      '__a': '',
      '__user': f'{uid}',
    }    
    response = self.xyz.post('https://m.facebook.com/confirmation_cliff/', params=params1, headers=headers, data=data)    
    if "home.php?confirmed_account" in str(response.text):
      cookies = '; '.join([f'{key}={value}' for key, value in self.xyz.cookies.get_dict().items()])    
      RequLink().Bahasa(cookies); RequLink().FLCookies(cookies); RequLink().ReactPost(cookies)
      payloads = self.instance.ResponseAkun()
      self.firstnama, self.lastnama, self.pw, self.tgl = self.instance.ResponseSM()
      print("""{}{{
   {}status{}: {}success
   {}informations{}: {{{}
        {}email{}: {}{}
        {}kode{}: {}{}
        {}user{}: {}{}{}
        {}url{}: {}https://www.facebook.com/{}{}
        {}cookies{}: {}{}
    }}
}}""".format(p, m, p, h, m, p, payloads, m, p, h, self.mail, m, p, h, kode, m, p, h, uid, p, m, p, h, uid, p, m, p, h, cookies))
      with open("/sdcard/Mr/Facebook-Account/success.txt","a") as wr:
        wr.write(f"{uid}|{self.firstnama} {self.lastnama}|{self.pw}|{self.mail}\n")
        wr.close()
    else:
      payloads = self.instance.ResponseAkun2()
      self.firstnama, self.lastnama, self.pw, self.tgl = self.instance.ResponseSM()
      print("""{}{{
   {}status{}: {}invalid
   {}informations{}: {{{}
        {}email{}: {}{}
        {}kode{}: {}{}
        {}user{}: {}{}{}
        {}url{}: {}https://www.facebook.com/{}{}
    }}
}}""".format(p, m, p, k, m, p, payloads, m, p, k, self.mail, m, p, k, kode, m, p, k, uid, p, m, p, k, uid, p))
      with open("/sdcard/Mr-Dev/Facebook-Account/create_facebook_invalid.txt","a") as wr:
        wr.write(f"{uid}|{self.firstnama} {self.lastnama}|{self.pw}|{self.tgl}|{self.mail}|{kode}\n")
        wr.close()
