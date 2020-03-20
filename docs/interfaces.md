#### 接口文档

##### 排行榜

- `URL`:/api/client/leader_board

- 请求方式：`GET`

- 功能：查看排行榜

- 响应码：10000为正确值

- 参数列表

  | 参数名 | 类型   | 必须  | 解释                     |
  | ------ | ------ | ----- | ------------------------ |
  | start  | int    | False | 查看排行榜开始位置 默认0 |
  | end    | int    | False | 查看排行榜结束位置 默认0 |
  | client | string | True  | 客户端名                 |

- 请求示例

  ```
  /api/client/leader_board?start=10&end=20&client=客户端2
  ```

- 响应

  ```json
  {
      "info": [
          {
              "order": 1,
              "client": "客户端2",
              "score": 20
          },
          {
              "order": 2,
              "client": "客户端3",
              "score": 15
          },
          {
              "order": 3,
              "client": "客户端1",
              "score": 10
          },
          {
              "order": 3,
              "client": "客户端1",
              "score": 10
          }
      ],
      ""code": 10000
  }
  ```

- 请求方式：`POST`

- `content-type`:form-data

- 功能：上传分数

- 响应码：10000为正确值

- 参数列表

  | 参数名 | 类型   | 必须  | 解释                     |
  | ------ | ------ | ----- | ------------------------ |
  | score  | int    | True | 正整数                    |
  | client | string | True  | 客户端名                 |

- 请求示例

  ```
  /api/client/leader_board
  ```

- 响应

  ```json
  {
      "info": {
          "info": "客户端3 : success update score"
      },
      "code": 10000
  }
  ```
  
  

