import React from 'react';
import Card from 'react-bootstrap/Card';
import Button from 'react-bootstrap/Button';

const ImageCard = ({ image, deleteImage }) => {
  // Debug: log the image object to see its structure
  console.log('ImageCard received image:', image);

  // Safety checks for image properties
  const imageUrl =
    image?.urls?.small || image?.urls?.regular || image?.urls?.raw || '';
  const imageTitle = image?.title || image?.alt_description || 'Untitled';
  const imageDescription =
    image?.description || image?.alt_description || 'No description available';

  return (
    <Card style={{ width: '18rem' }}>
      {imageUrl ? (
        <Card.Img variant="top" src={imageUrl} />
      ) : (
        <div
          style={{
            height: '200px',
            backgroundColor: '#f8f9fa',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
          }}
        >
          <span>No image available</span>
        </div>
      )}
      <Card.Body>
        <Card.Title>{imageTitle.toUpperCase()}</Card.Title>
        <Card.Text>{imageDescription}</Card.Text>
        <Button variant="primary" onClick={() => deleteImage(image.id)}>
          Delete
        </Button>
      </Card.Body>
    </Card>
  );
};

export default ImageCard;
