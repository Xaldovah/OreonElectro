import React, { useState, useEffect } from 'react';
import axios from 'axios';

interface ProfileData {
  user: string;
  shipping_address: string;
  billing_address: string;
  phone_number: string;
}

const Profile: React.FC = () => {
  const [profileData, setProfileData] = useState<ProfileData | null>(null);

  useEffect(() => {
    const fetchProfile = async () => {
      try {
        const response = await axios.get<ProfileData>('/api/customer/');
        setProfileData(response.data);
      } catch (error) {
        console.log(error);
      }
    };

    fetchProfile();
  }, []);

  return (
    // Will add user profile display here
  );
};

export default Profile;
