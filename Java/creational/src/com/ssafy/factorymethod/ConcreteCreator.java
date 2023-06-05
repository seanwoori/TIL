package com.ssafy.factorymethod;
public class ConcreteCreator extends Creator {
    
    protected Product factoryMethod() {
        return new ConcreteProduct();
    }
}