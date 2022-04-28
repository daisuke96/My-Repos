

# ■サービス概要
EC2：仮想サーバーの作成、利用が可能
S3：データ保存、静的なコンテンツ配信が可能
RDS：データベースが利用可能
IAM：権限管理、ユーザー管理が可能

## EC2
### SSH接続手順
1．key pairの作成

- EC2インスタンスへSSHログインするために必要
 
 1-1．IAMユーザーでログイン（csvに記載されているURL）

- EC2よりキーペアから作成可能

2．セキュリティグループの作成

- デフォルトでは外部からのアクセスが遮断されている
- SSHも不可

    【アクセスルール】

    ・インバウンド：外→内

    ・アウトバウンド：内→外

    ※基本的にインバウンドのみ制限、アウトは無制限が多い

★その他
- パブリックIPは起動ごとにに代わる
- VSCODEとかと紐づけているときはconfig注意！
→elastic ipを使えば固定化可能→お金かかる…

### VSCODEとの接続
- CONFIGファイルを手で作らない！！

  https://qiita.com/takao-takass/items/9f81d5095924280966ae


## S3
1．バケット（ストレージ）を作成
2．バケット内にファイルをアップロード可能、ダウンロードも可能
3．オブジェクトURLにアクセスすると通常はエラーになるが、公開することも可能
→ウェブサイトのホスティング、アクセス許可、
ホスティング：indexページの設定が可能
アクセス許可：オブジェクト（バケット）、ページごとに制限が可能（ネットへの公開非公開設定	）

【EC2からS3を操作する】
1．rootユーザーでマイセキュリティ資格からアクセスキーを作成する
2．作成したキーをダウンロード
3．SSH接続後、下記を入力
aws configure --profile poweruser
この後４つ入力を求められるため、以下の通り入力。
AWS Access Key ID [None]:（Access key IDのセルの下にある文字列）
AWS Secret Access Key [None]:（Secret access keyのセルの下にある文字列）
Default region name [None]: ap-northeast-1
Default output format [None]: json

4．aws --profile poweruser s3　で操作が可能
例）バケットの一覧を表示する  
aws --profile poweruser s3 ls

※上記アクセスキーの設定はプロファイルとアクセスキーを紐づけることでAWSサービス間の操作を可能にしている
コンソール上での権限＝プロファイルを別途作成し、存在するroot,IAMユーザーのアクセスキーと紐づけ
コンソールがプロファイル（どのユーザーの権限なのか）を選ぶ感じ
誤ってrootのアクセスキーを付与してしまうと大変



■バケットの削除
バケット内のファイルを削除する必要あり


■RDS
DBのサービス、IAMユーザーで実行するには権限が必要
IAMからインラインポリシーの追加を選択
→DB作成

■IAM
グループの作成を行うことで権限を分けることができる
→サービス単位やサービスの操作ごとに可能
「グループ」から作成が可能

※EC2インスタンスは起動していないと他IAMユーザーから見れない？
★リージョン注意！（DB、EC2どれもリージョンごとに作成している）
IAM等共通のものもある

■Billing
コスト管理サービス
→使用料等を確認できるサービス

■Lambda
サーバーレスコンピューティングが可能なサービス
→通常Webサーバー等のサーバーを立てるが、その必要がなく、PGだけ用意すればよい
→また、ほかのサービスの動作をトリガーにして処理させることも可能

■Role
お面のようなもの、ユーザー以外のものに権限を付与できる
→Roleを付与するにはPassRoleの権限が必要（ユーザーごと）
例：IAMユーザーでLambda作成時に対象関数にRoleを付与する→PassRoleの権限が必要
https://dev.classmethod.jp/articles/iam-role-passrole-assumerole/
→研修ではs3を操作できるRoleをrootユーザーで作成し、そのRoleをLambda（関数）に付与した


■Lambda
ログの書き込みには関数に付与しているロールに「AWSLambdaBasicExecutionRole」を追加する必要あり
＋cloud watchのLogGroupにaws/lambda/【関数名】を作る必要あり

lambda実行時のjson例は下記
{
	"Records": [
		{
			"eventVersion": "2.1",
			"eventSource": "aws:s3",
			"awsRegion": "ap-northeast-1",
			"eventTime": "2022-03-24T08:33:28.700Z",
			"eventName": "ObjectCreated:Put",
			"userIdentity": {
				"principalId": "AWS:hoge"
			},
			"requestParameters": {
				"sourceIPAddress": "xxx.xxx.xxx.xxx"
			},
			"responseElements": {
				"x-amz-request-id": "hoge",
				"x-amz-id-2": "hoge"
			},
			"s3": {
				"s3SchemaVersion": "1.0",
				"configurationId": "hoge",
				"bucket": {
					"name": "mybucket-20220324",  //バケット名
					"ownerIdentity": {
						"principalId": "hoge"
					},
					"arn": "arn:aws:s3:::mybucket-20220324"
				},
				"object": {
					"key": "import/test.txt",  //バケットから見た相対パス
					"size": 5,
					"eTag": "hoge",
					"sequencer": "hoge"
				}
			}
		}
	]
}


■APIgateway
APIの作成公開が容易に行えるサービス、セキュリティも高い
Lambdaで関数を作成し、それを呼び出すことも可能
→メソッドの作成より紐づけが可能

【外部公開】
1．APIのデプロイから可能
2．ステージ名を入力し、デプロイ

【APIの削除】
ステージの削除を実行すればよい

■DynamoDB
サーバーレスなkey-value型のドキュメントデータベース
→Json等のドキュメント形式でデータを保持

【パーティション】
→グルーピングと似た意味
例：ある年のデータを月ごとにパーティションする

【インデックス（索引）】
データに効率よくアクセスする、下記2種が存在
ローカルセカンダリインデックス
→あるパーティションキーの中からAttributeを指定して抽出する
グローバルセカンダリインデックス
→全データの中からAttributeを指定して抽出する

■EC2にWordPressを立てる（Webアプリ構築）
sudo yum -y update
→yumの最新化

sudo reboot
→サーバー再起動

sudo /sbin/chkconfig httpd on
sudo service httpd start
→httpdの起動コマンド2つ連続

wget http://ja.wordpress.org/latest-ja.tar.gz ~/
→wordpressのインストール

tar xvzf ~/latest-ja.tar.gz
→gz圧縮ファイルの解凍

sudo cp -r ~/wordpress/* /var/www/html/
→wordpress/*ディレクトリの中身だけ指定（※wordpressフォルダは入らない）
sudo chown apache:apache -R /var/www/html/
→apache（httpd）プロセスがhtml配下に書き込みできるよう設定

★下記でwordpressを実行
（一つ目は初期設定のため無視）
http://[EC2インスタンスのパブリックDNS]/wp-admin/setup-config.php

http://ec2-xxxxxxx.ap-northeast-1.compute.amazonaws.com/wp-login.php

★AWSのIPが変わった際はDBのwp-optionsテーブルのsiteurl, homeのIPを変更する必要あり


★S3バケットの公開
ACLが編集無効になっている場合
→S3を触るのにACLとポリシー両方気にしないといけなかった
→デフォで無効にできるようになった
→ポリシーだけ編集すればおｋに

バケットのアクセス許可タブから
１．ブロックパブリックアクセスを無効に
２．バケットポリシーにて下記を設定（例）

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "Statement1",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::mybucket-20220324/*"
        }
    ]
}


■WordPress(EC2)-RDS-S3の実装流れ
1．EC2を立てる
2．wordpressのインストール
3．RDSにてDBを作成
4. wordpressにてDBと接続
5．s3バケットを作成
6．wordpress内のプラグインからs3を登録、接続

※wordpress編集画面
http://ec2-54-250-202-199.ap-northeast-1.compute.amazonaws.com/wp-admin/edit.php?post_type=post


■ロール作成追記
IAMユーザーで作成する際は権限がないとダメっぽい

■DynamoDB-Lambda-APIGateway-user　によるサーバーレスアプリケーション構築

1．DynamoDBの作成
2．LambdaからDynamoDBを操作できるロールを作成
3．Lambdaの作成（DB操作記述）
4．APIGatewayの作成、設定（Lambdaとの紐づけ）
※あとからLambdaを作成してもエラーになる？
permissionエラーになった、おそらくAPI作成時(Lambda選択後)の権限付与しますか？チェックが影響してそう


■RESTAPI
リソースに対するメソッドを定義し、リソースをCRUD(post,get,put,delete)する
/リソース名/method(postなど)

■jsonデータをprintしたい場合
print(json.dumps(【jsonデータ変数】))

■pythonでdynamoDB CRUD操作
import json
import boto3
from boto3.dynamodb.conditions import Key

RESOURCE = 'dynamodb'
TABLE_NAME = 'sns_messages'#テーブル名
dynamodb = boto3.resource(RESOURCE)
table = dynamodb.Table(TABLE_NAME)

# テーブル内のレコードを全取得
def table_all():
    scanData = table.scan()
    items=scanData['Items']
    return scanData

# レコード追加・更新
def table_put(id, body, user):
    put_response = table.put_item(
        Item = {
            'id':id,
            'body':body,
            'user':user
        }
        
    )
    if put_response['ResponseMetadata']['HTTPStatusCode']==200:
        print('PUT Successed')
    else:
        print(put_response)
        
    return put_response

    
# レコード削除
def table_delete(id):
    delResponse = table.delete_item(
        Key = {
            'id':id
        }
        )
    if delResponse['ResponseMetadata']['HTTPStatusCode']==200:
        print('DELETE Successed')
    else:
        print(delResponse)
        
    return delResponse
    
#Lambdaから最初に呼びされるハンドラ関数
def lambda_handler(event, context):
    print("received event:"+json.dumps(event))

    try:
        if event['OperationType'] == 'ALL':
            return table_all()
        if event['OperationType'] == 'PUT':
            print("eventない表示")
            #json形式で受け取っているためdumpで整形
            print(json.dumps(event['Keys']['id']))
            return table_put(event['Keys']['id'],event['Keys']['body'],event['Keys']['user'])
        
        if event['OperationType'] == 'DELETE':
            print('method in')
            return table_delete(event['Keys']['id'])
        
        else:
            return None
        
    except Exception as e:
        print("Error Exception.")
        print(e)
■APIデプロイ後の動作確認方法
（URL発行後の動作確認方法？？）
→そもそもデプロイしてるのだからURL発行＝納品物では？
→テストはAPIGateway内で済ます
→デプロイ後はそのURLを使ってフロント(Vue.jsとか)とつなげるくらい？



■WebアプリケーションからDynamoDBの値を取得
Vue.js-APIGateway-Lambda-DynamoDB
1．APIGatewayにて対象APIのCORSを有効化する
2．デプロイ（ステージング）※デプロイしないと反映されない
3．VUe.jsからAPIGatewayを呼び出す
※axiosを使用、OperationTypeが異なる場合の書き方は不明、
PUTとかはAPIのテストで使っていたJSONをどこかで記載しそう
=============================
【テストデータ】
{
"OperationType": "PUT",
    "Keys": {
    "user":"tomo",
    "id":  "4",
    "body":"データを追加しました。"
    }
}
★下記の.post内にそのままいれればよさそう？
==========================================
【Vue.jsデータ】
<script>
import axios from 'axios';

export default {
  name: "App",
  data() {
  ～～～～
  },
  mounted() {
    axios
      .post("デプロイしたURL（リソース名までのURL）",{"OperationType":"ALL（PUT、DELETEとかも入る）"})
      .then(res => {
        this.items = res.data.Items;
      })
      .catch(err => {
        // eslint-disable-next-line
        console.log(err);
      });
  },
}
</script>