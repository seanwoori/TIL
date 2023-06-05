package com.ssafy.structural.proxy;

public class RealImage implements Image {

    private final String realImagePath;

    public RealImage(String imageName) {
        this.realImagePath = getImagePathFromAWS(imageName);
    }


    private String getImagePathFromAWS(String imageName) {
        return "/s3/image/" + imageName;
    }

    @Override
    public void displayImage() {
        System.out.println("Display Image Path : " + this.realImagePath);
    }
}