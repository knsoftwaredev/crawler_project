# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from sqlalchemy import MetaData, create_engine
from sqlalchemy import Table, Column, String, Text, Integer

class MecutiPipeline(object):

	def __init__(self):
		_engine = create_engine('sqlite:///mecuti_vn.db', echo=False)
		_connect = _engine.connect()
		_metadata = MetaData()
		_posts = Table('posts', _metadata,
			Column('id', Integer, primary_key=True),
			Column('title', Text),
			Column('url', Text),
			Column('content', Text)
		)
		_metadata.create_all(_engine)

		self.connect = _connect
		self.posts = _posts

	def process_item(self, item, spider):
		ins = self.posts.insert().values(
			title=item['title'], url=item['url'], content=item['content'])
		self.connect.execute(ins)
		return item
