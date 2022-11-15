import hvac
import sys
import json 

class VaultManager:

    def __init__(self) -> None:
        self.read_approle_token()
        self.vault_authenticate()

    def read_approle_token(self) -> None:
        with open('test') as file:
            self.config = json.load(file)

    def vault_authenticate(self) -> None:

        self.vault_client = hvac.Client(url=self.config['url'], namespace=self.config['ns'])

        self.vault_client.auth_cubbyhole(self.config['wrap_token'])

        #self.vault_client.is_authenticated()
        
        # try:
        #     self.vault_client.auth.approle.login(
        #         role_id=self.config['role_id'],
        #         secret_id=self.config['secret_id']
        #     )
        # except Exception as err:
        #     print(f"Failed authenticating to vault: {err}")


        self.vault_client.lookup_token()

    def vault_retrieve_credentials(self):
        read_response = self.client.secrets.kv.read_secret_version(path='my-secret-password')



def main():
    vm = VaultManager()

if __name__ == "__main__":
    main()
