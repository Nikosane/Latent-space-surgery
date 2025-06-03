class BaseVAE:
    def __init__(self, latent_dim):
        self.latent_dim = latent_dim

    def encode(self, x):
        raise NotImplementedError

    def decode(self, z):
        raise NotImplementedError

    def reparameterize(self, mu, logvar):
        raise NotImplementedError

    def loss_function(self, recon_x, x, mu, logvar):
        raise NotImplementedError
