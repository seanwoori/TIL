package com.ssafy.builder;

public class LombokExample {

	public static void main(String[] args) {
		LombokData trip = LombokData.builder()
	                .title("여행")
	                .nights(2)
	                .days(3)
	                .build();
		System.out.println(trip);
	 }

}
