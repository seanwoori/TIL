package com.ssafy.structural.flyweight;

//상수 풀
public class FlyweightInJava {

    public static void main(String[] args) {
        Integer i1 = Integer.valueOf(12000);
        Integer i2 = Integer.valueOf(12000);
        System.out.println(i1 == i2);
        System.out.println(i1.equals(i2));

        String s1 = "Design";
        System.out.println(s1.hashCode());
        String s2 = "Design";
        System.out.println(s2.hashCode());

        System.out.println("s1 s2 : " + (s1 == s2));
        System.out.println("s1 s2 : " + (s1.equals(s2)));

        String s3 = new String("hi");
        System.out.println(s3.hashCode());
        String s4 = "hi";
        System.out.println(s4.hashCode());

        System.out.println(s3 == s4);
        System.out.println(s3.equals(s4));

        // hashCode 같고, 주소 값은 다르다.
        // 상수풀에 들어가면 주소 값도 같아야 함.
    }
}