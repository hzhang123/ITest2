
接口自动化测试使用到的一些辅助工具类

## 使用说明

### http_client_manage

http请求，继承requests的Session并添加了一些断言

```
from itest2 import http_client_manage

# 创建客户端
http_client_manage.create_client(name="test", base_url="https://trains.ctrip.com")

# 获取客户端并发起请求，实际请求地址为https://trains.ctrip.com/trainBooking/ajax/getNotice
r = http_client_manage.get('/trainBooking/ajax/getNotice')
```

### db_client_manage

内置records库，只是添加了客户端查询管理的便捷方式，使用方法与返回结果遍历同records一致

```
from itest2 import db_client_manage

db_client_manage.create_clients('moon', 'postgresql://postgres:123456@127.0.0.1:5432/moon')
all = db_client_manage.client('moon').query('SELECT * FROM test_table LIMIT 10')
# 关闭链接
db_client_manage.close_all()
```

### Resource

文件资源管理

```
from itest2 import Resources
# 设置目录与文件扩展名称
rs = Resources(base_path='.', ext="json")
# 获取文件的绝对路径
rs.get_path('test')
# 获取json文件内容, 返回python 字典对象
rs.get_json('test')
```

### iwait

通过设置超时时间显示等待直到条件表达式成立/不成立或抛出异常。在一些异步接口、数据库修改、中间件结果验证时使用。

```
from itest2 import (http_client_manage, db_client_manage, iwait)

# 给定8s超时时间，默认每0.5s间隔请求1次test接口，直到返回状态码为200或到达超时时间抛出异常
iwait(http_client_manage, 8).until(lambda x: x.client('main').get('/test').status_code == 200)

# 给定10s超时时间，默认每0.5s间隔执行1次SQL，直到state字段为activated或到达超时时间抛出异常
iwait(db_client_manage, 10).until_not(
    lambda x: x.client('default').query(
        'select state from table where id = 10')[0][0] == 'activated'
)
```

### json_schema

根据json 生成jsonschema或使用jsonschema校验json

```
from itest2 import json_schema

# jsonschema的生成与校验
instance = {"test": 1}
schema = json_schema.generate(instance)
json_schema.validate(instance, schema)】

# jsonschema文件的生成与使用文件校验
schema_file_path = './test_generate_and_validate_with_file.json'
instance = {"test": 1}
json_schema.generate_to_file(instance, schema_file_path)
json_schema.validate_from_file(instance, schema_file_path)
```