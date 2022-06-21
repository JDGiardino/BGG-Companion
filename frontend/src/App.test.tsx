import React from 'react';
import { render, screen } from '@testing-library/react';
import App from './App';

test('renders BGG', () => {
  render(<App />);
  const linkElement = screen.getByText(/BGG/i);
  expect(linkElement).toBeInTheDocument();
});
