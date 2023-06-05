package com.ssafy.builder;

public class ProductBuilderTest {

	public static void main(String[] args) {
	     Product comp = new Product.ProductBuilder("500 GB", "2 GB")
	                .setBluetoothEnabled(true)
	                .setGraphicsCardEnabled(true)
	                .build();
	     System.out.println(comp);
	}

}
