import { useState } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import Header from './components/Header';
import Search from './components/Search';
import ImageCard from './components/ImageCard';
import Welcome from './components/Welcome';
import { Container, Row, Col } from 'react-bootstrap';

// const UNSPLASH_KEY = process.env.REACT_APP_UNSPLASH_KEY;
const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:5000';

const App = () => {
  const [word, setWord] = useState('');
  const [images, setImages] = useState([]);

  const handleSearchSubmit = (e) => {
    e.preventDefault();
    console.log(word);
    fetch(
      // `https://api.unsplash.com/photos/random/?query=${word}&client_id=${UNSPLASH_KEY}`,
      `${API_URL}/new-image?query=${word}`,
    )
      .then((response) => response.json())
      .then((data) => {
        console.log('API Response:', data); // Debug log
        // The API returns search results, so we need to get the first result
        if (data && data.results && data.results.length > 0) {
          const imageData = data.results[0];
          setImages([{ ...imageData, title: word }, ...images]);
        } else {
          console.error('No images found in API response');
        }
      })
      .catch((error) => {
        console.log(error);
      });
    setWord('');
  };

  const handleDelete = (id) => {
    setImages(images.filter((image) => image.id !== id));
  };

  return (
    <div>
      <Header title="Images Gallery" />
      <Search word={word} setWord={setWord} handleSubmit={handleSearchSubmit} />
      <Container className="mt-4">
        {images.length ? (
          <Row xs={1} md={2} lg={3}>
            {images.map((image, i) => (
              <Col key={i} className="pb-3">
                <ImageCard image={image} deleteImage={handleDelete} />
              </Col>
            ))}
          </Row>
        ) : (
          <Welcome />
        )}
      </Container>
    </div>
  );
};

export default App;
