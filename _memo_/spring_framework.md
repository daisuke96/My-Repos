■Spring Frameworkメモ

■コア機能
・AOP:Aspect Oriented Programingアスペクト指向プログラミング
・DI(Dependency Injection)コンテナ（依存性の注入）

■AOP
中心的関心ごとと横断的関心ごとに分けてプログラムを作成
→共通機能とそれ以外で分けて作ろう？

■DIコンテナ
インターフェースをオーバーライドしてコンテナ(クラス)を作成
→必要なコンテナをすべて用意（クラス名は異なるが、メソッドはインターフェースと同じ）
→呼び出すとComponentがついたコンテナのみが処理される

例：
【インターフェース】
public interface Hoge{
    void huga(); //メソッドの側だけ用意
}

【コンテナ】
@Component //このコンテナを使用
public class ContenaName implements Hoge{ //implements後は元のインターフェース名
  @Override
  public void huga(){//インターフェース側で定義したメソッドを指定
      //コンテナ独自の処理
  }
}
※別ファイルで必要なだけコンテナを用意

【呼び出し】※メイン関数外でも可
1．インターフェースを注入
@Autowired
Hoge hoge; //インターフェース（クラス）名 インスタンス名（任意）で記載,
           //ここでインスタンス化されるのは、用意したコンテナの@Componentがついたクラス！！（ContenaNameを指定していない！）

private void execute(){//executeでメソッド呼び出し
    hoge.huga(); //上記インスタンス.メソッド名でメソッド呼び出し
}

★アノテーション(@hoge)を使うことでSpringBoot側にインスタンスの生成等を実行させることができる
→SpringBoot はnewを使わない

@Autowired
→インスタンスを該当箇所に注入

@Component
→インスタンスを生成する
→アプリ実行時にここを見に行き、インスタンス化する

---
その他MVCに関わるアノテーション
@Controller
→コントローラのインスタンス生成に使用
@Service
→ドメイン層の業務処理に使用
@Repository
→インフラストラクチャ層のDBアクセス処理に使用

※レイヤ
アプリケーション層：ユーザーとのデータ入出力制御
ドメイン層：APの中核メイン処理
インフラストラクチャ層：DB処理

