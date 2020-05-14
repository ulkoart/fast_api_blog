import sys
sys.path = ['', '..'] + sys.path[1:]

from core.db import Base
from blog.models import Post
from users.models import User
