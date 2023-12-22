from sqlalchemy import func, distinct
from sqlalchemy.orm import lazyload

def get_count(q):
	disable_group_by = False
	if len(q._entities) > 1:
		# currently support only one entity
		raise Exception('only one entity is supported for get_count, got: %s' % q)
	entity = q._entities[0]
	if hasattr(entity, 'column'):
		# _ColumnEntity has column attr - on case: query(Model.column)...
		col = entity.column
		if q._group_by and q._distinct:
			# which query can have both?
			raise NotImplementedError
		if q._group_by or q._distinct:
			col = distinct(col)
		if q._group_by:
			# need to disable group_by and enable distinct - we can do this because we have only 1 entity
			disable_group_by = True
		count_func = func.count(col)
	else:
		# _MapperEntity doesn't have column attr - on case: query(Model)...
		count_func = func.count()
	if q._group_by and not disable_group_by:
		count_func = count_func.over(None)
	count_q = q.options(lazyload('*')).statement.with_only_columns([count_func]).order_by(None)
	if disable_group_by:
		count_q = count_q.group_by(None)
	return q.session.execute(count_q).scalar()