# Checklist

## Plan
여러 장의 이미지를 목록으로 관리하고, index(또는 랜덤)에 해당하는 이미지 하나를 출력하는 ComfyUI 커스텀 노드. ComfyUI-Text-List의 이미지 버전.
- 입력: images(IMAGE_LIST 위젯, 업로드한 파일 이름 목록), index(INT, 0부터), random(On/Off)
- 출력: IMAGE, MASK (기본 Load Image 노드와 같은 형식)

## Tasks
- [x] 프로젝트 폴더 생성, git 초기화
- [x] 선택/로드 로직 구현 (`nodes.py`)
- [x] ComfyUI 등록 (`__init__.py`)
- [x] 썸네일 목록 + 업로드/삭제 위젯 (`web/image_list.js`)
- [x] 단위 테스트 작성 및 통과 (`tests/test_nodes.py`)
- [x] README 작성
- [x] 커밋
- [x] GitHub 저장소 생성 및 push
- [ ] ComfyUI PC에서 실제 동작 확인
