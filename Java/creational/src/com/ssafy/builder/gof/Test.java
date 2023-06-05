package com.ssafy.builder.gof;

public class Test {
	public static void main(String[] args) {
	    // 1. 포맷할 자바 데이터 생성
	    Data data = new Data("홍길동", 44);

	    // 2. 일반 텍스트로 포맷하여 출력하기
	    Builder builder1 = new PlainTextBuilder(data);
	    Director director1 = new Director(builder1);
	    String result1 = director1.build();
	    System.out.println(result1);

	    // 3. JSON 형식으로 포맷하여 출력하기
	    Builder builder2 = new JSONBuilder(data);
	    Director director2 = new Director(builder2);
	    String result2 = director2.build();
	    System.out.println(result2);

	    // 4. XML 형식으로 포맷하여 출력하기
	    Builder builder3 = new XMLBuilder(data);
	    Director director3 = new Director(builder3);
	    String result3 = director3.build();
	    System.out.println(result3);
	}
}
