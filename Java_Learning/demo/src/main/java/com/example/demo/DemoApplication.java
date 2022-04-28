package com.example.demo;

import com.example.demo.chapter03.used.Greet;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.beans.factory.annotation.Autowired;



@SpringBootApplication
public class DemoApplication {

	public static void main(String[] args) {
		SpringApplication.run(DemoApplication.class, args)
		.getBean(DemoApplication.class).execute();

	}

	/**
	 * 注入される箇所（インターフェース）
	 * componentがついている方のクラスをインスタンス化＆注入
	 */
	@Autowired
	Greet greet;

	/**
	 * 実行メソッド
	 * 注入されたインスタンスのメソッドを実行
	 */

	 private void execute(){
		 greet.greeting();
	 }

}
