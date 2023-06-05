package com.ssafy.factorymethod;
public class FactoryMethodClient {
    
    public FactoryMethodClient(Creator creator) {
        Product product = creator.createOperation();
        System.out.println(product.aMethod());
    }
}