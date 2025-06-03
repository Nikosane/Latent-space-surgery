class BaseGAN:
    def __init__(self, latent_dim):
        self.latent_dim = latent_dim

    def build_generator(self):
        raise NotImplementedError

    def build_discriminator(self):
        raise NotImplementedError

    def train(self, data_loader):
        raise NotImplementedError

