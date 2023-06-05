package com.ssafy.structural.proxy;

public class ProxyImage implements Image {

    private RealImage realImage;
    private final String imageName;

    public ProxyImage(String imageName) {
        this.imageName = imageName;
    }

    @Override
    public void displayImage() {
        if (realImage == null) {
            realImage = new RealImage(imageName);
        }
        realImage.displayImage();
    }
}
