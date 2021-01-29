import pytest 
from data_transformer import translate


############################### TRANSLATION UNIT TESTS ###################################

@pytest.fixture
def translated_coords():
	test_object = ['palm_108_keypoints', 550.552, 2280.4, 621.377, 2209.57, 678.713, 2125.25, 722.557, 2013.96, 800.128, 1943.13, 638.241, 1990.35, 634.868, 1852.07, 614.632, 1761.01, 587.651, 1673.32, 564.042, 1986.98, 550.552, 1828.46, 543.806, 1720.54, 523.57, 1632.85, 499.962, 1986.98, 496.589, 1835.21, 489.844, 1747.52, 476.353, 1666.57, 439.254, 2003.84, 419.018, 1889.17, 419.018, 1828.46, 419.018, 1757.63]
	return translated_coords

@pytest.mark.translations
def test_translations_point_0(translated_coords):
	#point_0_x and point_0_y must = 0   
	assert all(coords == 0 for coords in translated_coords[1:3])


	
#@pytest.mark.translations
def test_translations_point_12_pass(translated_coords):
	#check x and y of point 12 
	assert translated_coords[37:39] == [26.982, -647.55]
	
#@pytest.mark.translations
def test_translations_point_15_fail(translated_coords):
	#coords of translated point_15 should be (-60.708, -532.88)
	assert translated_coords[46:48] == [239.39, -337.85]


############################### ENLARGEMENT UNIT TESTS ###################################

#@pytest.fixture
#def englarged_coords():
