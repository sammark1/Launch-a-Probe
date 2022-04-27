import * as THREE from 'three';
import render_data from './render_data.json' assert {type:'json'}


const displayElement = document.querySelector('#THREEJS1')
const displayZone = [innerWidth,500];

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75,displayZone[0]/displayZone[1], 0.1, 1000);
const renderer = new THREE.WebGLRenderer({antialias:true});
// const EC = new EffectComposer(renderer, camera);

renderer.setSize(displayZone[0],displayZone[1]);
renderer.setPixelRatio(devicePixelRatio);
document.getElementById("THREEJS1").appendChild(renderer.domElement);

const light1 = new THREE.PointLight( 0xffa000, .6, 100 )
const light2 = new THREE.PointLight( 0xffa0a0, .7, 100 )
const light3 = new THREE.PointLight( 0x2000ff, .5, 100 )
const testAmbLight = new THREE.AmbientLight( 0x500070, .25 )

const solarNoiseTexture = new THREE.TextureLoader().load('/static/images/solarNoiseTexture.png')
const solarAtmosTexture = new THREE.TextureLoader().load('/static/images/solarSubsufaceTexture.png')
const solarAtmosTexture2 = new THREE.TextureLoader().load('/static/images/solarAtmosphereTexture.png')
const icosphere = new THREE.IcosahedronGeometry(1,12);
const sphere = new THREE.SphereGeometry(1,24,24,)
const sphere2 = new THREE.SphereGeometry(1.01,24,24,)
const sphere3 = new THREE.SphereGeometry(1.02,24,24,)
let cubesphere = new THREE.BoxGeometry( 1, 1, 1, 6, 6, 6 )

const icoMaterial = new THREE.MeshPhongMaterial({
    color: render_data.bodyColor,
    bumpMap: solarNoiseTexture,
    emissiveMap: solarNoiseTexture,
    emissive: render_data.bodyColor,
});
const atmosMaterial = new THREE.MeshPhongMaterial({
    color: render_data.bodyColor,
    alphaMap: solarAtmosTexture,
    emissive: render_data.bodyColor,
});
atmosMaterial.transparent=true;
const atmosMaterial2 = new THREE.MeshPhongMaterial({
    color: render_data.bodyColor,
    alphaMap: solarAtmosTexture2,
    emissive: render_data.bodyColor,
    bumpMap: solarAtmosTexture,
});
atmosMaterial2.transparent=true;
//const icoMaterial = new THREE.LineBasicMaterial();
const body = new THREE.Mesh(sphere,icoMaterial);
const atmosphere = new THREE.Mesh(sphere2,atmosMaterial)
const atmosphere2 = new THREE.Mesh(sphere3,atmosMaterial2)

light1.position.set(0,12,0);
light2.position.set(12,8,10);
light3.position.set(-6,-12,0);

scene.add(body);
scene.add(atmosphere)
scene.add(atmosphere2)
scene.add(light1);
scene.add(light2);
scene.add(light3);
scene.add(testAmbLight)

light1.target = body;

camera.position.z = 3;


function animate () {
    requestAnimationFrame(animate);
    renderer.render(scene, camera);
    // body.rotation.x +=0.007;
    body.rotation.y +=0.01;
    atmosphere.rotation.y +=0.005;
    atmosphere2.rotation.y +=0.005;
    // icoplanet.position.x+=0.02;
    // if (icoplanet.position.x>=8){
    //     icoplanet.position.x=-8;
    // }
}


animate()



