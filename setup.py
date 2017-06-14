from setuptools import setup

setup(
    name='simulate-input-macos',
    version='1.0',
    packages=['simulate_input_macos'],
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        siminput=simulate_input_macos.simulator:input
    ''',
)
