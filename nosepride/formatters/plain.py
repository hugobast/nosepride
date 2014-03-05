from .base import Base


class Plain(Base):

    format = "{0}{1}m{2}{3}"

    def generate_colors(self):
        return range(31, 37)
