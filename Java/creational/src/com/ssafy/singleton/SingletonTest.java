package com.ssafy.singleton;

public class SingletonTest {

	public static void main(String[] args) {
		Singleton o1 = Singleton.getInstance();
		Singleton o2 = Singleton.getInstance();
		
		System.out.println(o1);
		System.out.println(o2);

		
	}

}
