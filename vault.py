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

    def vault_authenticate(self, root_token=None) -> None:

        if root_token == None:
            self.vault_client = hvac.Client(url=self.config['url'], namespace=self.config['ns'], token=root_token)
        else:
            self.vault_client = hvac.Client(url=self.config['url'], namespace=self.config['ns'])
        
            try:
                self.vault_client.auth.approle.login(
                    role_id=self.config['role_id'],
                    secret_id=self.config['secret_id']
                )
            except Exception as err:
                print(f"Failed authenticating to vault: {err}")

        self.vault_client.lookup_token(token=self.config['secret_id'])

    def vault_retrieve_credentials(self):
        read_response = self.client.secrets.kv.read_secret_version(path='my-secret-password')

    def create_update_app_role(self) -> None:

        self.vault_client.auth.approle.create_or_update_approle(
            role_name="azure_app",
            token_policies=['app_policy'],
            token_type="service",
            token_ttl="60m",
            token_max_ttl="120m",
            token_num_uses=10
        )



def main():
    vm = VaultManager()

if __name__ == "__main__":
    main()
