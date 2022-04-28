package chapter02;
import java.util.ArrayList;
import java.util.List;


public class ListExercise {
    public static void main(String[] args){
        //String型を格納できるlistを用意
        List<String>names = new ArrayList<>();
        //string型のデータを格納する
        names.add("太郎");
        names.add("ジロウ");
        names.add("Saburo");

        for(String name:names){
            System.out.println(name);
        }
    }
}
