package com.ssafy.singleton;

public class Singleton {
	private static Singleton instance;
/*3.*/	
//	private static final Singleton INSTANCE = new Singleton();
	private Singleton() {}
	
	public static Singleton getInstance() {
		if(instance == null ) {
			 instance = new Singleton();
		}
		return instance;
	}
/*2.*/
//	public static synchronized Singleton getInstance() {
//		if(instance == null ) {
//			 instance = new Singleton();
//		}
//		return instance;
//	}

/*3.*/
//	public static Singleton getInstance() {
//		return INSTANCE;
//	}
	
/*4.*/
//	public static Singleton getInstance() {
//		if(instance == null ) {
//			synchronized (Singleton.class) {
//				 instance = new Singleton();
//			}
//		}
//		return instance;
//	}
}
