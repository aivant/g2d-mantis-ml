from setuptools import setup, find_packages 
import io

setup(	name='mantis-ml',
	version='1.5.5',
	author='Dimitrios Vitsios',
	author_email='dvitsios@gmail.com',
	description='Disease-agnostic gene prioritisation from high-throughput genomic screens by stochastic semi-supervised learning',
	url="https://github.com/astrazeneca-cgr-publications/mantis-ml-release",
	packages=find_packages(),
	python_requires='>=3.6',
	install_requires=['numpy==1.14.5',
			  'numpydoc==0.8.0',
			  'pandas==0.24.2',
 			  'scipy==1.2.1',
			  'scikit-learn==0.20.3',
		    	  'bokeh==1.1.0',
			  'h5py==2.9.0',
			  'tensorflow==1.10.0',
			  'Keras==2.2.4',
			  'matplotlib==3.0.3',
			  'palettable==3.1.1',
			  'plotly==3.9.0',
			  'PyYAML==5.1',
			  'seaborn==0.9.0',
			  'tables==3.5.1',
			  'twine==3.0.0',
			  'tqdm==4.14',
			  'umap-learn==0.3.8',
			  'xgboost==0.80'],
	include_package_data=True,
	entry_points={'console_scripts': ['mantisml=mantis_ml.modules.main.__main__:main',
					  'mantisml-profiler=mantis_ml.modules.profiler.__main__:main',
					  'mantisml-overlap=mantis_ml.modules.hypergeom_enrichment.__main__:main']}
)
