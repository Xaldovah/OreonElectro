import React from "react";

interface ImageProps {
  imgSrc: string;
  className?: string;
}

const Image: React.FC<ImageProps> = ({ imgSrc, className }) => {
  return <img className={className} src={imgSrc} alt={imgSrc} />;
};

export default Image;
