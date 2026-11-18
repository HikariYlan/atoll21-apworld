from test.bases import WorldTestBase

from ..world import Atoll21World


class Atoll21TestBase(WorldTestBase):
    game = "Atoll 21"
    world: Atoll21World
